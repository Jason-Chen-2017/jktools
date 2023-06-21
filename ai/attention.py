import torch
import torch.nn as nn
import torch.nn.functional as F

device = "cuda" if torch.cuda.is_available() else "cpu"

def test():
    # Example Usage:
    query, key, value = torch.randn(2, 3, 8, device=device), \
                        torch.randn(2, 3, 8, device=device), \
                        torch.randn(2, 3, 8, device=device)

    print(f'query=${query}')
    print(f'key=${key}')
    print(f'value=${value}')


    res = F.scaled_dot_product_attention(query, key, value)
    print(f'scaled_dot_product_attention res=${res}')


if __name__ == '__main__':
    test()
