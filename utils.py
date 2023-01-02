import meshplot as mp
import numpy as np
import matplotlib
import scipy.io
import h5py

def Visual_3D(v,f,c=np.array([241, 153, 159])/255,n="figure0",add_landmark=None,v_box_coods=None):
    #255, 166, 203
    p=mp.plot(v,f,c,plot=False)
    if add_landmark is not None:
        p.add_points(add_landmark,shading={"point_size": 5,"point_color": 'blue'})
    if v_box_coods:
        m=v_box_coods['m']
        ma=v_box_coods['ma']
        v_box = np.array([[m[0], m[1], m[2]], [ma[0], m[1], m[2]], [ma[0], ma[1], m[2]], [m[0], ma[1], m[2]],
                        [m[0], m[1], ma[2]], [ma[0], m[1], ma[2]], [ma[0], ma[1], ma[2]], [m[0], ma[1], ma[2]]])

        # Edges of the bounding box
        f_box = np.array([[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], 
                        [7, 4], [0, 4], [1, 5], [2, 6], [7, 3]], dtype=np.int)


        #p.add_edges(v_box, f_box, shading={"line_color": "#00ffffff"})
        p.add_points(v_box, shading={"point_color": "#00ffffff"})
    
    #p.remove_object(0)
    p.save(n)

def load_vf(file_path):
    mat=scipy.io.loadmat(file_path)
    return np.array(mat['pred_nodes']), np.array(mat['conn'])

def plot_contracting(v1,v2,cline,n="Time change"):
    p=mp.plot(v1,c=np.array([250, 77, 9])/255,shading={'point_size':0.2})
    p.add_points(v2,shading={'point_size':0.2})
    p.add_lines(v1,v2,shading={"line_color":cline})
    p.save(n)

def linear_mapping(v,vi=None,va=None):
    vmin=v.min()
    vmax=v.max()
    if vi is not None:
        vmin=vi
        vmax=va
    slope=1./(vmax-vmin)
    return (v-vmin)*slope