from fastapi import APIRouter, Response
from app.supabase.functions.invoice import get_sales, get_invoices_join_by_id
from app.core.pdf import create_pdf_invoice
from datetime import datetime
inv = APIRouter()


# Routes
@inv.get("/all")
def get_invoices():
    total_sales = 0
    sales = get_sales()
    for sale in sales:
        total_sales += sale["ventas"]
    
    return total_sales


@inv.get("/{inv_id}")
def get_invoice(inv_id: int):
    res = get_invoices_join_by_id(inv_id)
    res["created_at"] = datetime.fromisoformat(res["created_at"]).strftime("%d/%m/%Y")
    pdf = create_pdf_invoice(res)
    return Response(content=pdf, media_type="application/pdf", headers={"Content-Disposition": f"attachment; filename=invoice_{inv_id}.pdf"})
