#
# This file is part of RHEVM-API. RHEVM-API is free software that is made
# available under the MIT license. Consult the file "LICENSE" that is
# distributed together with this file for the exact licensing terms.
#
# RHEVM-API is copyright (c) 2010 by the RHEVM-API authors. See the file
# "AUTHORS" for a complete overview.

from rhevm.api import powershell
from rhevm.collection import RhevmCollection


class DataCenterCollection(RhevmCollection):

    name = 'datacenters'
    objectname = 'datacenter'

    def show(self, id):
        """Show one resource. GET /collection/{id}"""
        filter = self._filter_from_dict({'DataCenterId': id})
        result = powershell.execute('Select-DataCenter | %s' % filter)
        if result:
            return result[0]

    def list(self, **filter):
        """Show all resources. GET /collection"""
        filter = self._filter_from_dict(filter)
        result = powershell.execute('Select-DataCenter | %s' % filter)
        return result

    def create(self, id, input):
        """Add a resource to the collection. POST /collection."""
        cmdline = self._cmdline_from_dict(input)
        result = powershell.execute('Create-DataCenter %s' % cmdline)
        return result[0]['DataCenterId']

    def update(self, id, input):
        """Update a resource in the collection. PUT /collection/{id}."""
        filter = self._filter_from_args({'DataCenterId': id})
        result = powershell.execute('Select-DataCenter | %s' % filter)
        if not result:
            raise KeyError
        powershell.execute('$dc = Select-DataCenter | %s' % filter)
        for key in input:
            powershell.execute('$dc.%s = "%s"' % (key, value))
        powershell.execute('Update-DataCenter -DataCenterObject $dc')

    def delete(self, id):
        """Delete a resource from the collection. DELETE /collection/{id}."""
        filter = self._filter_from_dict({'DataCenterId': id})
        result = powershell.execute('Select-DataCenter | %s' % filter)
        if not result:
            raise KeyError
        powershell.execute('Remove-DataCenter -DataCenterId %s' % id)
