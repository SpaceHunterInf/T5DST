#!/bin/bash
# Name of the job
#SBATCH -J neo
# Number of GPU
#SBATCH --gres=gpu:rtx_6000_ada:2
# time: 48 hours
#SBATCH --time=5:0:0
# Number of cpus
#SBATCH --cpus-per-task=2
# Log output
#SBATCH -e ./log/slurm-err-%j.txt
#SBATCH -o ./log/slurm-out-%j.txt
#SBATCH --open-mode=append
#SBATCH --array=0
# Start your application
eval "$(conda shell.bash hook)"

lang=turkish
saving_dir=output/$lang
python T5.py \
  --train_batch_size 8 \
  --GPU 2 \
  --slot_lang slottype \
  --n_epochs 3 \
  --saving_dir $saving_dir \
  --data_dir data/dst_$lang(base)