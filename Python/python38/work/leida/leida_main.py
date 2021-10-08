
import cinrad

path = r'F:/file/work/leida/'
file = path + 'Z_RADR_I_Z9250_20160701001000_O_DOR_SA_CAP.bin'
f_lei = cinrad.io.CinradReader(file)
r = f_lei.get_data(0, 400, "REF")
cinrad.visualize.PPI(r)

