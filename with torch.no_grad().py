with torch.no_grad():
    logits = model(mfcc_tensor.unsqueeze(0))  # [1, T, D]
    pred = torch.argmax(logits, dim=2)  # [1, T]
    pred = pred.squeeze().tolist()

# CTC decoding (remove repeated and blank)
output = []
prev = -1
for p in pred:
    if p != prev and p != 0:  # 0 = blank
        output.append(int_to_char[p])
    prev = p

print("Танылған:", ''.join(output))
