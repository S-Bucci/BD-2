# Validaciones comunes
import re

def validar_email(email):
    if not email or not isinstance(email, str):
        return False
    
    # Patrón regex para validar email
    patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron_email, email.strip()))


def validar_telefono(telefono):
    if not telefono or not isinstance(telefono, str):
        return False
    
    # Remover espacios y caracteres comunes de formato
    telefono_limpio = re.sub(r'[\s\-\(\)\+]', '', telefono.strip())
    
    # Verificar que solo contenga dígitos y que tenga entre 8 y 15 dígitos
    if not telefono_limpio.isdigit():
        return False
    
    return 8 <= len(telefono_limpio) <= 15
