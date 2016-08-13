#--- tool package ---#
import os
import random
import math
import config

init_weight = 0.05
# random.seed(10)

def next_init_weight():
	return (random.random() - 0.5) * init_weight

# convert string list to integer array [yzx]
def ints(data):
	int_array = []
	for d in data:
		int_array.append(int(d))
	return int_array

# convert to string list
def strings(data):
	str_array = []
	for d in data:
		str_array.append(`d`)
	return str_array

# sigmoid function
def sigmoid(z):
	value = 0.5
	try:
		value = 1.0 / (1.0 + math.exp(-z))
	except:
		# print "Math Out of Range. " + `z`
		value = 1E-9
	return value

def estimate_ctr(weight, feature, train_flag = False):
	value = 0.0
	for idx in feature:
		if idx in weight:
			value += weight[idx]
		elif train_flag:
			weight[idx] = next_init_weight()
	ctr = sigmoid(value)
# 	print "Estimated CTR \t" + `ctr`
	return ctr

def calibrate_ctr(pctr, ds_ratio):
	cal_pctr = pctr / (pctr + (1 - pctr) / ds_ratio)
	return cal_pctr

def gen_performance_line(log):
	performance = log['performance']
	line = `performance['revenue']` + "\t" \
			+ `performance['roi']` + "\t" \
			+ `performance['ctr']` + "\t" \
			+ `performance['cpc']` + "\t" \
			+ `performance['auc']` + "\t" \
			+ `performance['rmse']` + "\t" \
			+ `performance['cpm']` + "\t" \
			+ `performance['bids']` + "\t" \
			+ `performance['imps']` + "\t" \
 			+ `performance['clks']`
 	return line

def judge_stop(logs):
	stop = False
	# step = int(1/config.train_progress_unit)
	step = 1
	curr_loop = len(logs) - 1 # the latest record id
	if curr_loop >= 2*step:
		current_r = logs[curr_loop]['performance']['revenue']
		last_r = logs[curr_loop - step]['performance']['revenue']
		last_2_r = logs[curr_loop - 2*step]['performance']['revenue']
		# print "Curr:last:last_2 = " + `current_r` + ":" + `last_r` + ":" + `last_2_r`
		if current_r < last_r and last_r < last_2_r:
			stop = True
	return stop

def extend_judge_stop(logs):
	stop = False
	if len(logs) < 10:
		stop = False
	else:
		stop = judge_stop(logs)
	return stop

def get_last_log(logs):
	return logs[len(logs)-1]

#--- no use below ---#

# load data from file as [[yzx]]
def load_data(file_path):
	dataset = []
	if not os.path.isfile(file_path):
		print "ERROR: file not exist. " + file_path
	else:
		fi = open(file_path, 'r')
		for line in fi:
			li = ints(line.replace(':1','').split())
			dataset.append(li)
		fi.close()
	return dataset
