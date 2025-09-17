<h1>IMPORTANTE</h1>

Extensibilidad
- Arquitectura modular + inyección de dependencias
- Patrón Strategy para almacenamiento
- Nuevas páginas y servicios sin modificar código existente
- Soporte para distintas bases de datos

Funciones (Usuario Final)
- Catálogo: agregar, editar, eliminar productos (nombre, precio, stock, descripción)
- Ventas: carrito, validación de stock, finalizar transacción
- Reportes: historial de ventas (ID, fecha, ingresos, costos, ganancias)
- Notificaciones: SnackBar para errores/confirmaciones
- Persistencia: JSON + logging + manejo de errores

Guía para Desarrolladores
1. Crear nueva página UI en `ui/pages/`
2. Implementar servicio de negocio
3. Extender `BaseStorage` y su implementación
4. Integrar en `MainView` con navegación
5. Actualizar `main.py` con dependencias

Buenas Prácticas
- Separación de capas: UI / Servicios / Storage
- Validación de datos antes de operaciones
- Manejo de errores centralizado con logging
