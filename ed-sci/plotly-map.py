# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:51:46 2019

@author: svsti
"""
import pandas as pd
import plotly.plotly as py

early_ed = pd.read_csv('net_enrollment.csv', na_values='..').dropna(thresh=8)
early_ed['average_enrollment'] = early_ed.mean(axis=1, skipna=True, numeric_only=True)

data = [ dict(
        type = 'choropleth',
        locations = early_ed['country_code'],
        z = early_ed['average_enrollment'],
        text = early_ed['country'],
        colorscale = [
        [
          0,
          "rgb(37, 52, 148)"
        ],
        [
          0.30000000000000004,
          "rgb(8, 104, 172)"
        ],
        [
          0.4,
          "rgb(44, 127, 184)"
        ],
        [
          0.5,
          "rgb(65, 182, 196)"
        ],
        [
          0.65,
          "rgb(161, 218, 180)"
        ],
        [
          1,
          "rgb(255, 255, 204)"
        ]
      ],
        autocolorscale = False,
        reversescale = True,
        marker = dict(
            line = dict (
                color = 'rgb(0,0,0)',
                width = 0.75
            ) ),
        colorbar = dict(
            autotick = False,
            ticksuffix = '%',
            title = 'Net Enrollment %'),
      ) ]

layout = dict(
    title = 'Average Net Enrollment in Pre-K',
    geo = dict(
        showframe = True,
        showcoastlines = True,
        projection = dict(
            type = 'Mercator'
        )
    )
)

fig = dict( data=data, layout=layout )
py.plot(fig, validate=False, filename='early-ed-map' )