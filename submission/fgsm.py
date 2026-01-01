import torch
import torch.nn.functional as F

class FGSMAttack:
    def __init__(self, model, epsilon):
        self.model = model
        self.epsilon = epsilon

    def generate(self, image, label):
        image.requires_grad = True
        output = self.model(image)
        loss = F.nll_loss(output, label)
        self.model.zero_grad()
        loss.backward()
        grad = image.grad.data
        perturbed_image = image + self.epsilon * grad.sign()
        return torch.clamp(perturbed_image, 0, 1)
