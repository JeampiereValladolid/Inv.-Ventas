import flet as ft
from ui.main_view import MainView
from services.inventory_service import InventoryService
from services.sales_service import SalesService
from storage.json_storage import JSONStorage
from utils.logger import setup_logger


def init_services(logger):
    """Inicializa capa de almacenamiento y servicios."""
    storage = JSONStorage()
    inventory_service = InventoryService(storage)
    sales_service = SalesService(storage, inventory_service)
    return inventory_service, sales_service


def main(page: ft.Page):
    """
    Punto de entrada de la aplicación.
    Configura la interfaz y carga los servicios.
    """
    page.title = "Inventario Productos"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.window_width, page.window_height = 1200, 800
    page.window_min_width, page.window_min_height = 800, 600
    page.padding = 0

    logger = setup_logger()

    try:
        inventory_service, sales_service = init_services(logger)
        main_view = MainView(page, inventory_service, sales_service)
        page.add(main_view)
    except Exception as e:
        logger.error(f"Error al inicializar la aplicación: {e}")
        page.add(ft.Text(f"Error crítico al iniciar la aplicación: {e}", color="red"))

    page.update()


if __name__ == "__main__":
    ft.app(target=main)