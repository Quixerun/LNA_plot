import ipywidgets as widgets
values = [1, 1.25, 1.5, 1.75,
          2, 2.25, 2.5, 2.75,
          3, 3.25, 3.5, 3.75,
          4]
c = 0

class DataSetManager:
    def __init__(self):
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
        
        my_slider_1.observe(self.on_index_1_change, names="index")
        my_slider_2.observe(self.on_index_2_change, names="index")
        
        display(my_slider_1)
        display(my_slider_2)
        
    def update(self):
        global c
        c = [self.VGS1, self.VGS2]
        
    def on_index_1_change(self, change):
        self.VGS1 = change['new']
        self.update()
        
    def on_index_2_change(self, change):
        self.VGS2 = change['new']
        self.update()
