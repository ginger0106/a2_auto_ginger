import os
import numpy as np

PATH = '/home/ginger/a2_auto/client/traces'
trace = {}

def region():
    trace_lst = []

    for region in os.listdir(PATH):
        if region.startswith('re'):
            path = os.path.join(PATH,region)
            for num in range(6):

                content_path = os.path.join(path,f'content_{num}.npy')
                print(content_path)
                trace_lst.append(np.load(content_path))
            trace[region] = np.sum(trace_lst)
            trace_lst = []
    print(trace)

def content():
    trace_lst = []

    for num in range(6):
        for region in os.listdir(PATH):
            if region.startswith('re'):
                path = os.path.join(PATH,region)

                content_path = os.path.join(path,f'content_{num}.npy')
                # print(content_path)
                trace_lst.append(np.load(content_path)[:])
        trace[num] = np.sum(trace_lst)
        trace_lst = []
    print(trace)
# content()

def gen_trace():
    trace_lst = [6]*20+[10]*20+[2]*680
    print(trace_lst)
    np.save('/home/ginger/a2_auto/client/traces/region_0/content_8.npy',trace_lst)

content()
