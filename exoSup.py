import mysql.connector
import pandas as pd

def transform_pizza_dataset():
    # Connexion à la base de données
    connection = mysql.connector.connect(
        host='localhost',
        user='votre_utilisateur',  # Remplacez par votre nom d'utilisateur MySQL
        password='votre_mot_de_passe',  # Remplacez par votre mot de passe
        database='votre_base_de_donnees'  # Remplacez par le nom de votre base de données
    )
    
    # Requête SQL complexe de transformation
    query = """
    SELECT 
        # Conserve toutes les colonnes d'origine
        *,
        
        # Remplacement des valeurs nulles dans pizza_category par 'Classic'
        COALESCE(pizza_category, 'Classic') AS pizza_category,
        
        # Remplacement des valeurs nulles de quantity par sa moyenne
        COALESCE(quantity, ROUND((SELECT AVG(quantity) FROM ventes_pizza WHERE quantity IS NOT NULL))) AS quantity,
        
        # Nettoyage et standardisation de pizza_size
        CASE 
            # Trim des espaces et conversion en majuscules
            WHEN TRIM(UPPER(pizza_size)) IN ('M', 'L', 'S', 'XL', 'XXL') THEN TRIM(UPPER(pizza_size))
            # Remplacement des valeurs incorrectes par le mode (valeur la plus fréquente)
            ELSE (
                SELECT TRIM(UPPER(pizza_size)) 
                FROM ventes_pizza 
                WHERE TRIM(UPPER(pizza_size)) IN ('M', 'L', 'S', 'XL', 'XXL')
                GROUP BY TRIM(UPPER(pizza_size))
                ORDER BY COUNT(*) DESC 
                LIMIT 1
            )
        END AS pizza_size
    FROM ventes_pizza
    """
    
    try:
        # Exécution de la requête et chargement dans un DataFrame
        df = pd.read_sql(query, connection)
        
        # Conversion de quantity en entier
        df['quantity'] = df['quantity'].astype(int)
        
        return df
    
    except mysql.connector.Error as err:
        print(f"Erreur MySQL: {err}")
    
    finally:
        # Fermeture de la connexion
        connection.close()

# Utilisation de la fonction
pizza_dataframe = transform_pizza_dataset()
print(pizza_dataframe)
