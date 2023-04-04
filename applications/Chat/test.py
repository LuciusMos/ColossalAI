import torch

a = torch.tensor([[[1, 2, 3], [3, 4, 5]], [[-1, 2, -3], [3, -4, 5]]], dtype=torch.float32)
print(a.shape, a)
a = a[:, :-1]
print(a.shape, a)
print(a.mean(dim=1).squeeze(1).shape, a.mean(dim=1).squeeze(1))
print(a.mean(dim=1).squeeze(1).shape, a.mean(dim=1))
