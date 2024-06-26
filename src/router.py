from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastui import FastUI, prebuilt_html

from src.ui import dairy_page, home_page

router = APIRouter()


@router.get("/api/", response_model=FastUI, response_model_exclude_none=True)
async def main_page():
    """
    Main page of the app.
    """
    return dairy_page(home_page(), title="Dairy")


@router.get("/{path:path}")
async def html_landing():
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title="Dairy"))
