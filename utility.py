import numpy as np 





def MUB_gen(nq=1):
	"""
	Generates a mutually unbiased basis for a qubit system.
	"""

	# compute dimension
	dim = 2**nq
	# preallocate MUB array (keep as state vectors for efficiency)
	MUB = np.zeros((dim,dim,dim+1),dtype=np.complex128)


	return MUB

def SQST(rho, povm, sample_num):
	"""
	Performs the SQST protocol on a given density operator using the supplied POVM and 
	desired sample number
	"""	

	# retrieve problem dimension 
	dim = len(rho)

	# generate a random vector of basis choices (to simulate the POVM) in one go 
	basis_choice = random.choice(dim+1, size=sample_num, replace=True)

	# preallocate measurement outcome array
	measurement_outcomes = np.zeros((2,sample_num), dtype=np.uint16)

	# iterate over each choice of measurement basis
	for base_index in basis_choice:
		# extract uniformaly chosen basis
		basis = povm[:,:,base_index]
		# compute probabilities for measurement in that basis
		projection_right = np.einsum()
		projection_left = 
		basis_probs = abs(projection_left )**2
		basis_probs = np.einsum("ij,ijk", rho, basis)
		# randomly select outcome according to that distribution


	