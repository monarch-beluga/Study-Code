#ifndef GDAL_RASTER_ADD_H
#define GDAL_RASTER_ADD_H

#include <gdal_priv.h>
#include <cpl_conv.h>
#include <string>

using std::string;

int raster_add(string file1, string file2, string outfile)
{
    GDALAllRegister();
    try {
        GDALDataset *ds1 = (GDALDataset *) GDALOpen(file1.c_str(), GA_ReadOnly);
        GDALDataset *ds2 = (GDALDataset *) GDALOpen(file2.c_str(), GA_ReadOnly);

        int x_size, y_size;
        x_size = ds1->GetRasterXSize();
        y_size = ds1->GetRasterYSize();

        GDALRasterBand *band1 = ds1->GetRasterBand(1);
        GDALRasterBand *band2 = ds2->GetRasterBand(1);

        CPLErr errcode;
        float *data1, *data2, nodata_1, nodata_2;
        nodata_1 = band1->GetNoDataValue();
        nodata_2 = band2->GetNoDataValue();
        int numPix = x_size * y_size;
        data1 = new float[numPix];
        data2 = new float[numPix];
        errcode = band1->RasterIO(GF_Read, 0, 0, x_size, y_size, data1, x_size, y_size, GDT_Float32, 0, 0);
        errcode = band2->RasterIO(GF_Read, 0, 0, x_size, y_size, data2, x_size, y_size, GDT_Float32, 0, 0);

        int nodata_count;
        float *data_mean = new float[numPix];
        for (int i = 0; i < numPix; i++)
        {
            nodata_count = 0;
            if (data1[i] != nodata_1)
                nodata_count += 1;
            if (data2[i] != nodata_2)
                nodata_count += 2;
            switch (nodata_count)
            {
                case 0:
                    data_mean[i] = nodata_1;
                    break;
                case 1:
                    data_mean[i] = data1[i];
                    break;
                case 2:
                    data_mean[i] = data2[i];
                    break;

                default:
                    data_mean[i] = (data1[i] + data2[i]) / 2;
                    break;
            }
        }

        char **options = NULL;
        options = CSLSetNameValue(options, "COMPRESS", "LZW");
//        options = CSLSetNameValue(options, "TILED", "YES");
        GDALDriver *poDriver = ds1->GetDriver();
        GDALDataset *dst = poDriver->CreateCopy(outfile.c_str(), ds1, TRUE, options, NULL, NULL);
        GDALRasterBand *band3 = dst->GetRasterBand(1);
        errcode = band3->RasterIO(GF_Write, 0, 0, x_size, y_size, data_mean, x_size, y_size, GDT_Float32, 0, 0);

        delete[] data1;
        delete[] data2;
        delete[] data_mean;
        GDALClose(ds1);
        GDALClose(ds2);
        GDALClose(dst);
    } catch (string e) {
        return 1;
    }
    return 0;
}

#endif // GDAL_RASTER_ADD_H
