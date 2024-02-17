from sentence_transformers import SentenceTransformer
import numpy as np
import app.supabase.functions.foods as food_table
from numpy import dot
from numpy.linalg import norm


class CoreRecommendation:

    def __init__(self) -> None:
        self.products = self.get_products()
        # Utiliza un modelo preentrenado.
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        # self.save_product_vectors()

    def get_products(self):
        products = food_table.get_foods_without_products()
        return products
      
    def get_product_by_id(self, product_id):
        for product in self.products:
            if product['id'] == product_id:
                return product

    def cosine_similarity(self, v1, v2):
        return dot(v1, v2) / (norm(v1) * norm(v2))

    def get_text_for_product(self, product):
        """ 
        product fields: id, name, price, description
        """
        text = ""
        text += f"name: {product['name']}\n"
        text += f"price: {product['price']}\n"
        text += f"description: {product['description']}\n"
        return text

    def embedding_sentence_transformers(self, text):
        try:
            # Genera el embedding utilizando sentence-transformers
            embedding = self.model.encode(text, convert_to_tensor=True)
            # Convierte el tensor a un array de numpy y luego a bytes para almacenarlo
            return embedding.numpy().tobytes()
        except Exception as e:
            print(e)
            return None

    def extension_products_vector(self):
        if self.products and len(self.products) != 0:
            counter = 0
            for product in self.products:
                counter += 1
                text = self.get_text_for_product(product)
                product['vector'] = self.embedding_openai(text)
            return True
        return False

    def recommended_products(self, products, top_k=2):
        text = ""
        for product in products:
            text += product + "\n"
        query_vector = self.embedding_sentence_transformers(text)
        # Asegúrate de que query_vector sea un ndarray antes de pasarlo
        query_vector = np.frombuffer(query_vector, dtype=np.float32)
        similar_products_ids = self.find_similar_products(query_vector, top_k)
        
        products = []
        for product_id, similarity in similar_products_ids:
            products.append(self.get_product_by_id(product_id))
            
        return products

    def save_product_vectors(self):
        products = self.get_products()
        for product in products:
            text = self.get_text_for_product(product)
            vector = self.embedding_sentence_transformers(text)
            product['vector'] = np.frombuffer(
                vector, dtype=np.float32).tolist()
            updated_product = {
                'id': product['id'], 'vector': product['vector']}
            food_table.save_vector_food(updated_product)

    # Función para encontrar productos similares

    def find_similar_products(self, query_vector, top_k=5):
        # Obtener todos los vectores de productos
        all_product_vectors = food_table.get_all_vector_foods()

        # Calcular la similitud con todos los productos
        similarities = {}
        for product in all_product_vectors:
            product_id = product['product_id']
            vector = product['vector']
            # Convertir el arreglo de floats a bytes
            vector_bytes = np.array(
                vector, dtype=np.float32).tobytes()
            # Convertir bytes a ndarray
            product_vector = np.frombuffer(vector_bytes, dtype=np.float32)
            # Calcular similitud del coseno
            similarity = self.cosine_similarity(query_vector, product_vector)
            similarities[product_id] = similarity

        # Ordenar los productos por similitud
        sorted_similarities = sorted(
            similarities.items(), key=lambda item: item[1], reverse=True)

        # Devolver los top K productos más similares
        return sorted_similarities[:top_k]
