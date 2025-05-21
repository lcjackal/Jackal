import shutil

@router.get("/settings/export")
def export_settings():
    shutil.copy(SETTINGS_PATH, SETTINGS_PATH+".bak")
    with open(SETTINGS_PATH, "rb") as f:
        return Response(f.read(), headers={"Content-Disposition": "attachment; filename=settings.json"}, media_type="application/json")

@router.post("/settings/import")
def import_settings(file: UploadFile = File(...)):
    with open(SETTINGS_PATH, "wb") as f:
        f.write(file.file.read())
    return {"status": "imported"}