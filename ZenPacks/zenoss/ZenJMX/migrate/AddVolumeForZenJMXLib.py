##############################################################################
#
# Copyright (C) Zenoss, Inc. 2021, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################


import Globals
from Products.ZenModel.migrate.Migrate import Version
from Products.ZenModel.ZenPack import ZenPack, ZenPackMigration

import logging
log = logging.getLogger("zen.migrate")

zenjmx_libs_containerPath = "/opt/zenoss/zenjmx-libs"
zenjmx_libs_owner = "zenoss:zenoss"
zenjmx_libs_permission = "0755"
zenjmx_libs_resourcePath = "zenjmx-libs"


class AddVolumeForZenJMXLib(ZenPackMigration):
    version = Version(3, 13, 1)

    def migrate(self, dmd):
        log.info("Add volume for zenjmx-libs")
        try:
            import servicemigration as sm
            sm.require("1.1.5")
        except ImportError:
            log.debug("Couldn't import servicemigration, skipping")
            return

        try:
            ctx = sm.ServiceContext()
        except sm.ServiceMigrationError:
            log.debug("Couldn't generate service context, skipping")
            return

        volume_exist = False
        created = False

        for inst in (s for s in ctx.services if 'zenjmx' in s.name):
            for volume in inst.volumes:
                if volume.containerPath == zenjmx_libs_containerPath:
                    volume_exist = True
                    log.debug("Volume for zenjmx-libs already exists")
                    break
            if not volume_exist:
                inst.volumes.append(sm.volume.Volume(
                    containerPath=zenjmx_libs_containerPath,
                    owner=zenjmx_libs_owner,
                    permission=zenjmx_libs_permission,
                    resourcePath=zenjmx_libs_resourcePath
                ))
                created = True

        if created:
            log.info("Volume for zenjmx-libs created")
            ctx.commit()


AddVolumeForZenJMXLib()
