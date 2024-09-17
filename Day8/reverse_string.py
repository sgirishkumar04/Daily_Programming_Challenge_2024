def reverse(s: str) -> str:
    words = s.split()
    reversed = words[::-1]
    return ' '.join(reversed)

print(reverse("the sky is blue"))         
print(reverse("  hello world  "))      
print(reverse("a good   example"))       
print(reverse("    "))                  
print(reverse("word"))                 
