#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clasificador de Temas para Comentarios de Campañas
Personalizable por campaña/producto
"""

import re
from typing import Callable


def create_topic_classifier() -> Callable[[str], str]:
    """
    Retorna una función de clasificación de temas personalizada para esta campaña.
    
    Returns:
        function: Función que toma un comentario (str) y retorna un tema (str)
    
    Usage:
        classifier = create_topic_classifier()
        tema = classifier("¿Dónde puedo comprar este producto?")
        # tema = 'Preguntas sobre el Producto'
    """
    
    def classify_topic(comment): 
        comment_lower = str(comment).lower()

        if re.search(r'\bcar[oó]|\bprecio\b|\bval[eé]|\bcosto\b|\bcu[aá]nto vale|\b4200\b|\b100 pesos?\b|costoso|estafa|injusto|lujo', comment_lower):
            return 'Precio y Valoración Económica'

        if re.search(r'espeso|agu[ao]|tra[ei]a? m[aá]s|trae menos|contenido|hojuelas|mitad|vac[ií]o|disminuy[oó]|calidad|cantidad|cambia[rd]o|ahora|antes|antigua', comment_lower):
            return 'Cambios en Calidad/Producto'

        if re.search(r'recuerdo|infancia|niñez|niñ[oa]|hace [0-9]+|1988|35 años|marcando|cuando era|bob yurt|morenitas|navidad|tajalapiz', comment_lower):
            return 'Experiencia y Nostalgia'

        if re.search(r'sabor|rico|delicioso|maluco|pesimo|remedio|diabetes|az[uú]car|dulce|espesito|sabe a', comment_lower):
            return 'Sabor y Características'

        if re.search(r'kevin johansen|eduardo niño|chocapic|diseño|publicidad|promoci[oó]n|inteligencia artificial|ai\b|bon yurt morenitas', comment_lower):
            return 'Campaña Publicitaria'

        if re.search(r'\bdónde comprar|\bcomprar\b|disponible|tiendas|consigo|promoción|pregunta|duda|\bcomo se|\bpara qué', comment_lower):
            return 'Preguntas sobre el Producto'

        if re.search(r'\b(mierda|basura|estafa|car[oó] y mal[ou])\b', comment_lower):
            return 'Comentarios Negativos'

        if re.search(r'am[eé]n|jajaja|bendiciones|^\W*$', comment_lower) or len(comment_lower.split()) < 3:
            return 'Fuera de Tema / No Relevante'

        return 'Otros'
    
    return classify_topic


# ============================================================================
# METADATA DE LA CAMPAÑA (OPCIONAL)
# ============================================================================

CAMPAIGN_METADATA = {
    'campaign_name': 'Alpina - BonYurt Morenitas',
    'product': 'BonYurt Morenitas',
    'categories': [
        'Precio y Valoración Económica'
        'Cambios en Calidad/Producto'
        'Experiencia y Nostalgia'
        'Sabor y Características',
        'Campaña Publicitaria',
        'Preguntas sobre el Producto',
        'Comentarios Negativos',
        'Fuera de Tema / No Relevante',
        'Otros'
    ],
    'version': '1.0',
    'last_updated': '2025-11-24'
}


def get_campaign_metadata() -> dict:
    """Retorna metadata de la campaña"""
    return CAMPAIGN_METADATA.copy()
