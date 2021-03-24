import pandas as pd 
import numpy as np 

def avg_odo():
    # Get Odometer and Cylinder Columns.
    df_veh = pd.read_csv('vehicles.csv', usecols= ['odometer','cylinders'])
    # Replace blanks and drop NaN rows.
    df_veh['odometer'].replace(' ', np.nan, inplace=True)
    df_veh.dropna(subset=['odometer'], inplace=True)
    # Get 6 cylinder vehicles
    df_six = df_veh.loc[df_veh['cylinders']=='6 cylinders']
    # Convert odometer rows to float
    df_six['odometer'] = pd.to_numeric(df_six['odometer'])
    # Get the average.
    print(df_six.odometer.mean())

def avg_suv_price():
    # Get Type and Price Columns.
    df_veh = pd.read_csv('vehicles.csv', usecols=['price','type'])
    # Remove all non-zero price rows. 
    df_veh['price'].replace(0, np.nan, inplace=True)
    df_veh.dropna(subset=['price'], inplace=True)
    # Get 6 cylinder vehicles
    df_six = df_veh.loc[df_veh['type']=='SUV']
    # Convert odometer rows to float
    df_six['price'] = pd.to_numeric(df_six['price'])
    # Get the average.
    print(df_six.price.mean())

def avg_truck_pickup():
    df_veh = pd.read_csv('vehicles.csv', usecols=['price','type'])
    # Get Type and Price Columns.
    df_veh['price'].replace(0, np.nan, inplace=True)
    df_veh.dropna(subset=['price'], inplace=True)
    # Get trucks and pickups
    df_p = df_veh.loc[df_veh['type']=='pickup']
    df_t = df_veh.loc[df_veh['type']=='truck']
    # Combine trucks and pickups together.
    df_pt = pd.concat([df_p, df_t])
    # Convert to float
    df_pt['price'] = pd.to_numeric(df_pt['price'])
    print(df_pt.price.mean())


def fuel_veh_manu():
    df_veh = pd.read_csv('vehicles.csv', usecols=['manufacturer','fuel'])
    # Remove blanks NaN and some other errors in the fuel column.
    df_veh['manufacturer'].replace(' ', np.nan, inplace=True)
    df_veh['fuel'].replace(' ', np.nan, inplace=True)
    df_veh['fuel'].replace(' 1-Series', np.nan, inplace=True)
    df_veh['fuel'].replace(' BMW', np.nan, inplace=True)
    df_veh['fuel'].replace(' Ml Class', np.nan, inplace=True)
     
    df_veh.dropna(subset=['manufacturer'], inplace=True)
    df_veh.dropna(subset=['fuel'], inplace=True)
    # 
    print(df_veh.groupby(['manufacturer','fuel'])['fuel'].count())
    
fuel_veh_manu()