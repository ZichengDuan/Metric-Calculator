import numpy as np
import os
from pyeval.calAOS import evaluateDetectionAPAOS

def evaluate(res_fpath, gt_fpath):
    import matlab.engine
    eng = matlab.engine.start_matlab()
    eng.cd('motchallenge-devkit')
    res = eng.evaluateLocation(res_fpath, gt_fpath)
    recall, precision, moda, modp = np.array(res['detMets']).squeeze()[[0, 1, -2, -1]]
    AP_50, AOS_50, OS_50, AP_25, AOS_25, OS_25 = evaluateDetectionAPAOS(res_fpath, gt_fpath)
    return recall, precision, moda, modp, AP_50, AOS_50, OS_50, AP_25, AOS_25, OS_25

if __name__ == "__main__":
    res_fpath = os.path.abspath('results.txt')
    gt_fpath = os.path.abspath('gt.txt')

    recall, precision, moda, modp, AP_50, AOS_50, OS_50, AP_25, AOS_25, OS_25 = evaluate(res_fpath, gt_fpath)

    print("AP_50: %.1f" % AP_50, " ,AOS_50: %.1f" % AOS_50, ", OS_50: %.2f" % OS_50)
    print("AP_25: %.1f" % AP_25, " ,AOS_25: %.1f" % AOS_25, ", OS_25: %.2f" % OS_25)
