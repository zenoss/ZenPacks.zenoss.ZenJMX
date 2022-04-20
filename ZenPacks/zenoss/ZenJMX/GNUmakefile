##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2007, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


ZENJMX_HOME=$(PWD)
LIB_DIR=$(ZENJMX_HOME)/lib
TARGET=$(ZENJMX_HOME)/target

default: install


install:
	mvn assembly:assembly

	mkdir -p ${LIB_DIR} ; \
	cd ${LIB_DIR} ; \
	tar xzf ${TARGET}/*-bin.tar.gz

	cp ${ZENJMX_HOME}/src/main/resources/log4j.properties ${LIB_DIR}
	rm -rf ${TARGET}


clean:
	rm -rf ${LIB_DIR}
	rm -rf ${TARGET}
