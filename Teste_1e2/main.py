from src import data_transform
from src import webscrapper


def main():
    scrappe = webscrapper.WebScrapper(
        "https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss")
    scrappe.scrappe("Componente Organizacional")

    transform = data_transform.DataTransform()
    transform.transform("padrao-tiss_componente-organizacional_202111.pdf",
                        "./tables/table30.csv", [114])
    transform.transform("padrao-tiss_componente-organizacional_202111.pdf",
                        "./tables/table31.csv", [115, 116, 117, 118, 119, 120])
    transform.transform("padrao-tiss_componente-organizacional_202111.pdf",
                        "./tables/table32.csv", [120])
    transform.compress_files("./tables", "Teste_Jonatas_Rocha.zip")


if __name__ == '__main__':
    main()
