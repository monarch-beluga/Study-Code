# -*- coding:utf-8 _*-
"""
@version:
author:monarch
@time: 2021/10/12
@file: import_data.py
@function:
@modify:
"""

import pandas as pd
import pymysql
import geopandas as gpd
from sqlalchemy import create_engine


def create_table(year, database, sql_name, pwd, host, port):
    """

    Args:
        year: int, 气象数据年份
        database: str, 数据库名称, 默认为meteodata
        sql_name: str, mysql数据库用户名, 默认root
        pwd: str,  mysql数据库密码, 默认123456
        port: str, 数据库主机ip地址, 默认localhost
        host: int, 数据库端口, 默认3306

    Returns:

    """
    conn = pymysql.connect(host=host, password=pwd, port=port, user=sql_name, db=database)
    sql = f"CREATE table if not exists `all{year}` (Station Text,Year int,Month int,Day int,APRE real,DMXP real," \
          f" DMNP real, MTEM real,DMXT real,DMNT real,AVRH real,MNRH real, PREP real, MEWS real, MXWS real, DMWS real," \
          f" EXWS real,DEWS real, SOHR real,DATE Date, " \
          f"FLAG VARCHAR(40) primary key)ENGINE=InnoDB DEFAULT CHARSET = utf8"
    cour = conn.cursor()
    try:
        cour.execute(sql)
        conn.commit()
    except:
        conn.rollback()
    conn.close()


def station_import(filename: str, database='meteodata', sql_name='root', pwd='123456', host='localhost', port=3306):
    """

    Args:
        filename: str, 站点文件路径
        database: str, 数据库名称, 默认为meteodata
        sql_name: str, mysql数据库用户名, 默认root
        pwd: str,  mysql数据库密码, 默认123456
        port: str, 数据库主机ip地址, 默认localhost
        host: int, 数据库端口, 默认3306

    Returns: None

    """
    conn = create_engine(f'mysql+pymysql://{sql_name}:{pwd}@{host}:{port}/{database}', encoding='utf8')
    df = pd.read_csv(filename)
    df.columns = ['code', 'X', 'Y', 'elev', 'stationName', 'regionalName']

    df.to_sql('station', conn, if_exists='append', index=False)

    print('import station success !!!')


def me_data_import(filename: str, year: int, database='meteodata', sql_name='root', pwd='123456', host='localhost',
                   port=3306):
    """

    Args:
        filename: str, 气象数据文件路径
        year: int, 气象数据年份
        database: str, 数据库名称, 默认为meteodata
        sql_name: str, mysql数据库用户名, 默认root
        pwd: str,  mysql数据库密码, 默认123456
        port: str, 数据库主机ip地址, 默认localhost
        host: int, 数据库端口, 默认3306

    Returns: None

    """
    conn = create_engine(f'mysql+pymysql://{sql_name}:{pwd}@{host}:{port}/{database}', encoding='utf8')
    create_table(year, database, sql_name, pwd, host, port)
    data = pd.read_csv(filename, header=None)
    columns = ['Station', 'Year', 'Month', 'Day', 'APRE', 'DMXP', 'DMNP', 'MTEM', 'DMXT', 'DMNT', 'AVRH', 'MNRH',
               'PREP', 'MEWS', 'MXWS', 'DMWS', 'EXWS', 'DEWS', 'SOHR', 'DATE', 'FLAG']
    data[[1, 2, 3]] = data[[1, 2, 3]].astype(int)
    data[1] = data[1].astype(str)
    data[2] = data[2].apply(lambda x: format(x, '02d')).astype(str)
    data[3] = data[3].apply(lambda x: format(x, '02d')).astype(str)
    data['DATE'] = data[1] + '-' + data[2] + '-' + data[3]
    data['FLAG'] = data[0] + data[1] + data[2] + data[3]
    data[[1, 2, 3]] = data[[1, 2, 3]].astype(int)
    data.columns = columns
    data.drop_duplicates(subset=['Station', 'Year', 'Month', 'Day'], keep='first', inplace=True)

    data.to_sql(f'all{year}', conn, if_exists='append', index=False)

    print(f'{filename} import  success !!!')


def creat_station_shp(path: str, sql_name='root', pwd='123456', host='localhost', port=3306):
    """

    Args:
        path: shapefile文件生成路径
        sql_name: str, mysql数据库用户名, 默认root
        pwd: str,  mysql数据库密码, 默认123456
        port: str, 数据库主机ip地址, 默认localhost
        host: int, 数据库端口, 默认3306

    Returns:

    """
    f_names = ['ChinaStations.shp', 'ForeignStations.shp']
    dbs = ['meteodata', 'meteodata_extens']
    for f_name, db in zip(f_names, dbs):
        data = creat_station_geopandas(db, sql_name, pwd, host, port)
        data.to_file(f'{path}/{f_name}', encoding='utf-8')
        print(f"{f_name} creat success !!!")
    gdf = pd.concat([gpd.read_file(f'{path}/{shp}') for shp in f_names]).pipe(gpd.GeoDataFrame)
    gdf.to_crs('EPSG:4326')
    gdf.to_file(f'{path}/tStations.shp', encoding='utf-8')


def creat_station_geopandas(db: str, sql_name='root', pwd='123456', host='localhost', port=3306):
    """

    Args:
        db: str, 数据库名称, 默认为meteodata
        sql_name: str, mysql数据库用户名, 默认root
        pwd: str,  mysql数据库密码, 默认123456
        port: str, 数据库主机ip地址, 默认localhost
        host: int, 数据库端口, 默认3306

    Returns:
        data: GeoDataFrame

    """
    conn = pymysql.connect(host=host, password=pwd, port=port, user=sql_name, db=db)
    sql = f"select * from {db}.`station`"
    df = pd.read_sql(sql, conn).iloc[:, :5]
    df = df.loc[:, ['code', 'stationName', 'Y', 'X', 'elev']]
    data = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.X, df.Y), crs='EPSG:4326')
    data.columns = ['Code', 'Station', 'Lat', 'Lon', 'elev', 'geometry']
    data[['Lat', 'Lon', 'elev']] = data[['Lat', 'Lon', 'elev']].astype(float)
    conn.close()
    return data


def get_data_by_stations(stations: list, types: list, start_time: str, end_time: str, db: str, sql_name='root',
                         pwd='123456', host='localhost', port=3306):
    """

    Args:
        stations: list,
        types: list
        start_time: str,
        end_time: str,
        db: str
        sql_name: str, mysql数据库用户名, 默认root
        pwd: str,  mysql数据库密码, 默认123456
        port: str, 数据库主机ip地址, 默认localhost
        host: int, 数据库端口, 默认3306

    Returns:
        data: DataFrame
    """
    conn = pymysql.connect(host=host, password=pwd, port=port, user=sql_name, db=db)
    start_year = int(start_time.split('-')[0])
    end_year = int(end_time.split('-')[0])
    for year in range(start_year, end_year+1):
        sql = f'select Station, Year, Month, Day, {",".join(types)} from all{year} where ' \
              f'Station in ({str(stations).strip("[]")}) and DATE >= "{start_time}" and DATE <= "{end_time}"'
        df = pd.read_sql(sql, conn)
        if year == start_year:
            data = df
        else:
            data = pd.concat([data, df])
    return data


def get_data_by_shp(roi_shp, types: list, start_time: str, end_time: str, db: str, sql_name='root', pwd='123456',
                    host='localhost', port=3306):
    """

    Args:
        roi_shp: str / GeoDataFrame,
        types: list
        start_time: str,
        end_time: str,
        db: str
        sql_name: str, mysql数据库用户名, 默认root
        pwd: str,  mysql数据库密码, 默认123456
        port: str, 数据库主机ip地址, 默认localhost
        host: int, 数据库端口, 默认3306

    Returns:
        data: DataFrame
    """
    if type(roi_shp) == str:
        roi_df = gpd.read_file(roi_shp)
    else:
        roi_df = roi_shp
    gfd = creat_station_geopandas(db)
    geo = gpd.overlay(gfd, roi_df, 'intersection')
    stations = geo['Code'].tolist()
    data = get_data_by_stations(stations, types, start_time, end_time, db, sql_name, pwd, host, port)
    return data

