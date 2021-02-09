#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:08:54 2021

@author: kumardeepanshuverma
"""
import heapq
import os
class BinaryTreeNode:
    def __init__(self,value,freq):
        self.value=value
        self.freq=freq
        self.right=None
        self.left=None
    def __lt__(self,other):
        return self.frequency<self.other
    def __eq__(self,other):
        return self.frequency==self.other
class Huffmancoding:
    def __int__(self,path):
        self,path=path
        self.__heap=[]
        self.__codes={}
        self,__reversecodes=[]
    def __make_frequency_dict(self,text):
        freq_dict={}
        for char in text:
            if char not in freq_dict:
                freq_dict[char]=0
            freq_dict[char]+=1
        return freq_dict
    def __buildheap(self,freq_dict):
        for key in freq_dict:
            frequency=freq_dict[key]
            binarytreenode=BinaryTreeNode(key, frequency)
            heapq.heappush(self.__buildheap,binarytreenode)
    def __buildtree(self):
        while (len(self.__heap)>1):
            binarytree_node_1=heapq.heappop(self.__heap)
            binarytree_node_2=heapq.heappop(self.__heap)
            freq_sum=binarytree_node_1+binarytree_node_2
            newnode=BinaryTreeNode(None,freq_sum)
            newnode.left=binarytree_node_1
            newnode.right=binarytree_node_2
            heapq.heappushpop(self.__heap,newnode)
        return
    def __buildcodesHelper(self,root,curr_bits):
        if root is None:
            return
        if root.value is not None:
            self.__codes[root.value]=curr_bits
            self.__reversecodes[curr_bits]=root.value
            return
        self.__buildcodesHelper(root.left, curr_bits+"0")
        self.__buildcodesHelper(root.right, curr_bits+"1")
    def __buildcodes(self):
        root=heapq.heappop(self.__heap)
        self.__buildcodesHelper(root,"")
    def __getencodedtext(self,text):
        encoded_text=" "
        for char in text:
            encoded_text+=self.__codes[char]
        return encoded_text
    def compress(self):
        #Get the file from path
        #Read text from file
        #make freq dictionary using the text
        text="ncebedwdjeb"
        freq_dict=self.__make_frequency_dict(text)
        #Construct heap from freq_dict
        self.__buildheap(freq_dict)
        #construct the binary tree from heap
        self.__buildtree()
        #construct codes from the binary tree
        self.__buildcodes()
        #creating the encoded text using the codes
        encoded_text=self.__getencodedtext(text)
        #put this encoded text into the binary file
        #pad this encoded path
        #return this binary file as output
    