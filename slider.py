import ipywidgets as widgets
import math
import h5py
import numpy as np
values = [1, 1.25, 1.5, 1.75,
          2, 2.25, 2.5, 2.75,
          3, 3.25, 3.5, 3.75,
          4]
c = 0

class DataSetManager:
    
        
    def __init__(self):
        x = 13
        y = 13
        z = 2001
        with h5py.File("Lna_data.hdf5", "a") as f:
            K_calc_dset = f["K_calc"]
            Gmax_stable_dset = f["Gmax_stable"]
            Gmax_available_dset = f["Gmax_available"]
            freq_dset = f["frequency"]
        
            my_slider_1 = widgets.SelectionSlider(
                options=[str(_) for _ in values],
                value='2.5',
                description='Voltage 1',
                disabled=False,
                continuous_update=False,
                orientation='horizontal',
                readout=True
            )
            my_slider_2 = widgets.SelectionSlider(
                options=[str(_) for _ in values],
                value='2.5',
                description='Voltage 2',
                disabled=False,
                continuous_update=False,
                orientation='horizontal',
                readout=True
            )

            self.VGS1 = my_slider_1.index
            self.VGS2 = my_slider_2.index

            self.Data_k_calc = K_calc_dset[self.VGS1,self.VGS2,:]
            self.Data_Gmax_stable = Gmax_stable_dset[self.VGS1,self.VGS2,:]
            self.Data_Gmax_available = Gmax_available_dset[self.VGS1,self.VGS2,:]
            self.freq = freq_dset[:]

            my_slider_1.observe(self.on_index_1_change, names="index")
            my_slider_2.observe(self.on_index_2_change, names="index")

            display(my_slider_1)
            display(my_slider_2)
        quit()
    def update(self):
        global c
        c = [self.VGS1, self.VGS2]
        self.Data_k_calc = K_calc_dset[self.VGS1,self.VGS2,:]
        self.Data_Gmax_stable = Gmax_stable_dset[self.VGS1,self.VGS2,:]
        self.Data_Gmax_available = Gmax_available_dset[self.VGS1,self.VGS2,:]
        self.freq = freq_dset
        
    def on_index_1_change(self, change):
        self.VGS1 = change['new']
        self.update()
        
    def on_index_2_change(self, change):
        self.VGS2 = change['new']
        self.update()
    

       