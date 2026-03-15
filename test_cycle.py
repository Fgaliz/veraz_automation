from functions import *
import pytest



@pytest.mark.cycle
@pytest.mark.order(1)
def test_title():
    smoketest=SmokeTest()
    assert smoketest.fetch_title(url='https://fgaliz.github.io/proyecto_veraz/') == "Document Validation System"
    return 

#@pytest.mark.cycle
#@pytest.mark.order(2)
def test_get():
    assert fetch_document_data(url='https://api.bcra.gob.ar/centraldedeudores/v1.0/Deudas/', document_id='20949132049') is not None
    return