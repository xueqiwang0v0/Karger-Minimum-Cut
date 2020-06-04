#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 18:34:46 2020

@author: xueqiwang
"""

import random
import copy

def buildGraph(path):
    file = open(path)
    lines = file.readlines()
    file.close()
    
    graph = dict()
    
    for line in lines:
        temp = [int(num) for num in line.strip().split()]
        graph[temp[0]] = temp[1:]
    
    return graph

def kargerMinCut(graph):
    if len(graph.keys()) <= 2:
        return graph
    
    # pick a remaining edge randomly
    edges_lst = []
    for vertex in graph.keys():
        for edge in graph[vertex]:
            edges_lst.append((vertex, edge))
    
    u, v = random.choice(edges_lst)
    
    #print('u: ', u, u in graph.keys())
    #print('v: ', v, v in graph.keys())
    
    # merge u and v into a single vertex
    v_edges = graph.pop(v)
    u_edges = graph.pop(u)
    u_edges.extend(v_edges)
    
    # remove self-loops
    while u in u_edges:
        u_edges.remove(u)
    while v in u_edges:
        u_edges.remove(v)
    
    # update the graph
    for vertex in graph.keys():
        temp = graph[vertex]
        edges = [u if i==v else i for i in temp]
        graph[vertex] = edges
    graph[u] = u_edges
    
    return kargerMinCut(graph)
    
    

file = 'kargerMinCut.txt'
graph = buildGraph(file)

iterations = 500

min_cut = 100
while iterations >= 0:
    copied = copy.deepcopy(graph)
    temp_graph = kargerMinCut(copied)
    key = list(temp_graph.keys())[0]
    edges = len(temp_graph[key])
    
    if edges < min_cut:
        min_cut = edges
    
    iterations -= 1
    
    print(min_cut)
    
print(min_cut)