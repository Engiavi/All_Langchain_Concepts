import onnxruntime as ort

try:
    print("ONNX Runtime version:", ort.__version__)
    sess = ort.InferenceSession  # just check it's accessible
    print("ONNXRuntime loaded successfully.")
except Exception as e:
    print("ONNXRuntime failed to load:", e)
