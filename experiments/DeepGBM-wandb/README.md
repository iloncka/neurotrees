### Experiments with DeepGBM parameters on wine dataset with wandb.ai platform:

* for embeddings logged parameters:
    - 'emb_epoch': [2, 5, 10]
    - 'batch_size': [256, 128, 64, 32]
    - 'emb_lr': [1e-2, 1e-3, 1e-4, 3e-4, 3e-5, 1e-5]
    - 'optimizer': ['adamW', 'sgd']  
    
Notebook: embedding-wandb.ipynb  
Sweep page: https://wandb.ai/iloncka/deepgbm-wandb/sweeps/xzewnsyy  
Report: https://wandb.ai/iloncka/deepgbm-wandb/reports/Report-for-emb_epoch-batch_size-emb_lr-optimizer-parameters-tracking---VmlldzoxNTYwNzQ2   


* for embeddings logged parameters:
    - 'emb_epoch': [2, 5, 10]
    - 'batch_size': [256, 128, 64, 32]
    - 'emb_lr': [1e-2, 1e-3, 1e-4, 3e-4, 3e-5, 1e-5]
    - 'optimizer': ['adamW', 'sgd']  
    
Notebook: embedding-wandb-2.ipynb  
Sweep page: https://wandb.ai/iloncka/deepgbm-wandb/sweeps/r48kqhtn  
Report: https://wandb.ai/iloncka/deepgbm-wandb/reports/Report-for-emb_epoch-batch_size-emb_lr-optimizer-parameters-tracking-2---VmlldzoxNTYwODEy  

* for GBDT2NN logged parameters:
    - 'max_epoch': [20, 50, 100, 150]
    - 'batch_size': [512, 256, 128, 64]
    - 'lr': [1e-2, 1e-3, 1e-4, 3e-4, 3e-5, 1e-5]
    - 'l2_reg': [1e-2, 1e-3, 1e-4, 3e-4, 3e-5, 1e-5]
    - 'optimizer': ['adamW', 'sgd']  
    
Notebook: GBDT2NN-wandb.ipynb  
Sweep page: https://wandb.ai/iloncka/deepgbm-wandb/sweeps/8s53m07f  
Report: https://wandb.ai/iloncka/deepgbm-wandb/reports/Report-max_epoch-batch_size-lr-l2_reg-optimizer-parameters-tracking---VmlldzoxNTYwODMw  

* for GBDT2NN logged parameters:
    - 'max_epoch': 'values': [100, 150]
    - 'tree_layers': [[100,100,100,50], [100,100,50],[200,150,50], [50,50,50,50],]
    - 'optimizer': ['adamW', 'sgd']  
    
Notebook: GBDT2NN-wandb-2.ipynb  
Sweep page: https://wandb.ai/iloncka/deepgbm-wandb/sweeps/rexl5mud  
Report: https://wandb.ai/iloncka/deepgbm-wandb/reports/Report-for-max_epoch-optimizer-and-tree-layers-tracking--VmlldzoxNTU3MzU2  

Totals: 255 runs  
Project page: https://wandb.ai/iloncka/deepgbm-wandb
