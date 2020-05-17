import numpy as np
import ipyvolume as ipv

sample1 = np.memmap('D:\Docs\Python_code\FiberGen\sample1_8bit_256x256x256.raw',
                    shape=(256,256,256), dtype=np.uint8, mode='r')

m = ipv.volshow(sample1, lighting=False)
#ipv.show()

ipv.pylab.save('fibers_test_nonotebook.html', makedirs=True, title='IPyVolume Vol Render Fiber Test', all_states=False,
               offline=False, scripts_path='js', drop_defaults=False,
               template_options=(('extra_script_head', ''), ('body_pre', ''), ('body_post', '')),
               devmode=False, offline_cors=False)

