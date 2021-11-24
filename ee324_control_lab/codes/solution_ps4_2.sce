s = poly(0, 's')
function cl_tf_k = cltfk(K)
    // part a
    G = 10 / (s * (s + 2) * (s + 4))
    cl_tf_k = K * G / (1 + K * G)
endfunction

// part b
for k = 0:0.1:100
    tf = cltfk(k)
    poles = roots(tf.den)
    scatter(real(poles), imag(poles))
end

// part c
// my guess is k was around 5 when the poles cut the imaginary axis

// part d
tf = cltfk(5)
disp(routh_t(tf.den))
// the RH table has two sign changes, and the number causing the change is of the order of 10^-15
