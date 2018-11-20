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

#The histogram was split at the contig that represented N90.
#This is where all of the contigs of that length or longer have at least 90%
#of the sum of the length of all contigs. For this dataset, the value is 203657.
    
def get_n90(genome_data):
    total = genome_data["Length"].sum()
    print (genome_data[68:72])
    count = 0
    add = 0
    for num in genome_data["Length"]:
        count += 1
        add += num
        if add > total*0.9:
            break
    return count
        
def histograms(count, genome_data, ref_data):
    histo_full = sns.distplot(genome_data, bins = 20, kde = False, axlabel = 'Lengths')
    histo_full.set_title("Distribution of Assembly Data")
    plt.show()

    histo_split = sns.distplot(genome_data[count:], bins = 20, kde = False, axlabel = 'Lengths')
    histo_split.set_title("Distribution of Assembly Data Split")
    plt.show()
    

if __name__ == "__main__":
    lengths, ref_lengths = get_data()
    genome_data = pd.DataFrame({"Length": lengths})
    ref_data = pd.DataFrame({"Length": ref_lengths})
    cdf(genome_data, ref_data)
    count = get_n90(genome_data)
    histograms(count, genome_data, ref_data)
