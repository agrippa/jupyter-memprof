import gc
import time
from guppy import hpy

_hp = hpy()
_hp.setrelheap()

def big_objs(time_out_s = 60.0):
    h = _hp.heap()

    collect = []
    start_time = time.time()
    # TODO use bytype to filter out ipykernel and guppy objects?

    for p in range(len(h.bysize)):
        size_for_partition = h.bysize[p].size
        if size_for_partition > 32768:
            for i in range(len(h.bysize[p].byid)):
                obj = h.bysize[p].byid[i].shpaths[0]
                collect.append((str(obj), size_for_partition))

        elapsed_time = time.time() - start_time
        if elapsed_time > time_out_s:
            sys.stderr.write('WARNING: big_objs() exiting early -- ' +
                    'time_out_s = ' + str(time_out_s) + '\n')
            break

    return collect
