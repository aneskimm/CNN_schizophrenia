#just testing pytorch

# %%
# %%
import mne

file = "/Users/aneskimm/Desktop/neurals/cnn_schzpna/CNN_schizophrenia/dataset/dataverse_files/s01.edf"
data = mne.io.read_raw_edf(file, preload=True)
raw_data = data.get_data()

