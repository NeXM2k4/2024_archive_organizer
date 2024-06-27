import os

#RUTA A ORDENAR
downloads_folder = r"C:\Users\anexa\Downloads"

#RUTAS DE DESTINO
images_folder = r"C:\Users\anexa\Desktop\NeX\ALL_DOCS\IMAGES"
excel_folder = r"C:\Users\anexa\Desktop\NeX\ALL_DOCS\EXCEL_DOCS"
pdf_folder = r"C:\Users\anexa\Desktop\NeX\ALL_DOCS\PDF_DOCS"
word_folder = r"C:\Users\anexa\Desktop\NeX\ALL_DOCS\WORD_DOCS"
videos_folder = r"C:\Users\anexa\Desktop\NeX\ALL_DOCS\VIDEOS"
compress_folder = r"C:\Users\anexa\Desktop\NeX\ALL_DOCS\COMPRESS"

simulation_folder = r"C:\Users\anexa\Desktop\NeX\PROGRAMMING\USACO&ICPC\SIMULATIONS"

gofc_folder = r"C:\Users\anexa\Desktop\NeX\ALL_DOCS\JOVENES_TALENTO\2024\SABATINA"

#ORGANIZADOR
if __name__ == "__main__":
    for filename in os.listdir(downloads_folder):
        name, extension = os.path.splitext(os.path.join(downloads_folder, filename))
        
        #COMPROBACIÓN PARA NOMBRES
        
        if "SIMULATION" in name:
            os.rename(os.path.join(downloads_folder, filename),
                      os.path.join(simulation_folder, filename))
            
        elif "GOFC" in name:
            os.rename(os.path.join(downloads_folder, filename),
                      os.path.join(gofc_folder, filename))
        
        #COMPROBACIÓN PARA SOLO EXTENSIONES
        else:
            if extension.lower() in [".jpg", ".jpeg", ".png"]:
                os.rename(os.path.join(downloads_folder, filename), 
                          os.path.join(images_folder, filename))

            elif extension.lower() == ".xlsx":
                os.rename(os.path.join(downloads_folder, filename), 
                          os.path.join(excel_folder, filename))

            elif extension.lower() == ".pdf":
                os.rename(os.path.join(downloads_folder, filename), 
                          os.path.join(pdf_folder, filename))
                
            elif extension.lower() == ".docx":
                os.rename(os.path.join(downloads_folder, filename), 
                          os.path.join(word_folder, filename))
                
            elif extension.lower() == ".mp4":
                os.rename(os.path.join(downloads_folder, filename), 
                          os.path.join(videos_folder, filename))
                
            elif extension.lower() in [".zip", ".rar"]:
                os.rename(os.path.join(downloads_folder, filename), 
                          os.path.join(compress_folder, filename))
        