# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: LicenseRef-NONE

from java.lang.System import System
from java.lang.Object import Object


class SampleGetSystemInformations (Object):
    
    
    @classmethod
    def main (_ : type):
        p = System.getProperties();
        p.list(System.out);


SampleGetSystemInformations.main()
