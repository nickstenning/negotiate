from __future__ import absolute_import

from flask import abort, request, Response

from . import Negotiator as NegotiatorBase, negotiate as _negotiate
from . import Formatter as FormatterBase

__all__ = ['Negotiator', 'Formatter', 'negotiate']

class Negotiator(NegotiatorBase):
    def best_mimetype(self):
        return request.accept_mimetypes.best_match(self.accept_mimetypes, 'text/html')

    def _abort(self, status_code, err=None):
        return abort(status_code, err)


class Formatter(FormatterBase):
    def _make_response(self, body, content_type):
        return Response(body, content_type=content_type)


def negotiate(formatter_cls, *args, **kwargs):
    return _negotiate(Negotiator, formatter_cls, *args, **kwargs)
