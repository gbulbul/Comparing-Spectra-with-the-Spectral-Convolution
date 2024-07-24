# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 23:19:29 2024

@author: gbulb
"""
class Comparing_Spectra_with_the_Spectral_Convolution:
    def obtain_a_list_of_least_distances(S1,S2):
        difference=[100.000]
        all_possible=[]
        for i in range(len(S1)):
            for j in range(len(S2)):
                
                if abs(S1[i]-S2[j])<=min(difference):
                   
                   all_possible.append(round(abs(S1[i]-S2[j]),5))  
        return all_possible,max(all_possible)
    def find_the_frequency_of_most_common(all_possible):
        dict_={}
        for i,idx in enumerate(all_possible):
           counter=0
           if idx==all_possible[i] and i==i:
               while idx in all_possible:
                  dict_[idx]=counter
                  counter+=1
                  if counter >= (all_possible.count(idx)+1):
                     break
        return print(dict_)


if __name__=="__main__":               
    dict_={}
    S1=[186.07931, 287.12699, 548.20532, 580.18077, 681.22845, 706.27446, 782.27613, 968.35544, 968.35544]
    S2=[101.04768, 158.06914, 202.09536, 318.09979, 419.14747, 463.17369]
    all_possible,max_of_least_distances=Comparing_Spectra_with_the_Spectral_Convolution.obtain_a_list_of_least_distances(S1,S2)
    print(max_of_least_distances)
    Comparing_Spectra_with_the_Spectral_Convolution.find_the_frequency_of_most_common(all_possible)
    
        
    