from flex.core import load, validate, validate_api_call
from flex.http import Request, Response
import pytest

from .utils import authorize
from .. import factories


def normalize_request(req):
    return Request(
        url=req['PATH_INFO'],
        method=req['REQUEST_METHOD'].lower()
    )


def normalize_response(resp):
    return Response(
        request=resp.environ,
        content=resp.body,
        url='/municipality',
        status_code=resp.status_code,
        content_type=resp.headers['Content-Type'].split(';')[0],
        response=resp,
    )


@pytest.fixture
def schema(get):
    return load(get('/schema').json)


def validate_call(resp, schema):
    validate_api_call(schema,
                      normalize_request(resp.environ),
                      normalize_response(resp))


@authorize
def test_openapis_schema(get, schema):
    validate(schema)


@authorize
def test_get_municipality(get, schema):
    resource = factories.MunicipalityFactory()
    resp = get('/municipality/' + resource.id)
    validate_call(resp, schema)


@authorize
def test_get_municipality_collection(get, schema):
    factories.MunicipalityFactory()
    resp = get('/municipality')
    validate_call(resp, schema)


@authorize
def test_get_postcode(get, schema):
    resource = factories.PostCodeFactory()
    resp = get('/postcode/' + resource.id)
    validate_call(resp, schema)


@authorize
def test_get_postcode_collection(get, schema):
    factories.PostCodeFactory()
    resp = get('/postcode')
    validate_call(resp, schema)


@authorize
def test_get_group(get, schema):
    resource = factories.GroupFactory()
    resp = get('/group/' + resource.id)
    validate_call(resp, schema)


@authorize
def test_get_group_collection(get, schema):
    factories.GroupFactory()
    resp = get('/group')
    validate_call(resp, schema)


@authorize
def test_get_housenumber(get, schema):
    resource = factories.HouseNumberFactory()
    resp = get('/housenumber/' + resource.id)
    validate_call(resp, schema)


@authorize
def test_get_housenumber_collection(get, schema):
    factories.HouseNumberFactory()
    resp = get('/housenumber')
    validate_call(resp, schema)


@authorize
def test_get_position(get, schema):
    resource = factories.PositionFactory()
    resp = get('/position/' + resource.id)
    validate_call(resp, schema)


@authorize
def test_get_position_collection(get, schema):
    factories.PositionFactory()
    resp = get('/position')
    validate_call(resp, schema)
