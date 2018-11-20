import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def get_data():
    genome = open("data.txt")
    lengths = []
    for line in genome:
        line = line.split()
        if line == []:
            pass
        else:
            lengths.append(int(line[1]))
    lengths.sort(reverse=True)

    reference = open("reference.txt")
    ref_lengths = []
    for line in reference:
        line = line.split()
        if line == []:
            pass
        else:
            if int(line[1]) > 5000:
                ref_lengths.append(int(line[1]))
    ref_lengths.sort(reverse=True)
    return lengths, ref_lengths

def cdf(genome_data, ref_data):
    plt.plot(np.cumsum(genome_data), label = "Genome")
    plt.plot(np.cumsum(ref_data), label = "Reference")
    plt.legend()
    plt.show()

#The histogram was split at between contigs 17 and 18, because the contigs larger
#than that seem to be significantly greater than the rest of the contigs. By
#splitting here and this removing the outliers, the histogram is less skewed,
#allowing for a better visualization of the distribution. In addition, the N90 is
#statistic that is typically used to represent data.
    
def get_n90(genome_data):
    print (genome_data)
    total = genome_data["Length"].sum()
    count = 0
    add = 0
    for num in genome_data["Length"]:
        count += 1
        add += num
        if add > total*0.9:
            break
        
def histograms(genome_data, ref_data):
    histo_full = sns.distplot(genome_data, bins = 20, kde = False, axlabel = 'Lengths')
    histo_full.set_title("Distribution of Assembly Data")
    plt.show()

    histo_split = sns.distplot(genome_data[18:], bins = 20, kde = False, axlabel = 'Lengths')
    histo_split.set_title("Distribution of Assembly Data Split")
    plt.show()
    

if __name__ == "__main__":
    lengths, ref_lengths = get_data()
    genome_data = pd.DataFrame({"Length": lengths})
    ref_data = pd.DataFrame({"Length": ref_lengths})
    cdf(genome_data, ref_data)
    histograms(genome_data, ref_data)
