from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.decals.DecalBatch as _DecalBatch
_DecalBatch = _DecalBatch
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DecalBatch():
    """com.badlogic.gdx.graphics.g3d.decals.DecalBatch"""
 
    @staticmethod
    def _wrap(java_value: _DecalBatch) -> 'DecalBatch':
        return DecalBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DecalBatch):
        """
        Dynamic initializer for DecalBatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DecalBatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DecalBatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getSize(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.decals.DecalBatch.getSize()"""
        return int._wrap(super(DecalBatch, self).getSize())

    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalBatch.flush()"""
        super(DecalBatch, self).flush()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def initialize(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalBatch.initialize(int)"""
        super(_DecalBatch, self).initialize(_int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalBatch.dispose()"""
        super(DecalBatch, self).dispose()

    @overload
    def add(self, arg0: 'Decal'):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalBatch.add(com.badlogic.gdx.graphics.g3d.decals.Decal)"""
        super(_DecalBatch, self).add(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setGroupStrategy(self, arg0: 'GroupStrategy'):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalBatch.setGroupStrategy(com.badlogic.gdx.graphics.g3d.decals.GroupStrategy)"""
        super(_DecalBatch, self).setGroupStrategy(arg0)

    @overload
    def __init__(self, arg0: int, arg1: 'GroupStrategy'):
        """public com.badlogic.gdx.graphics.g3d.decals.DecalBatch(int,com.badlogic.gdx.graphics.g3d.decals.GroupStrategy)"""
        val = _DecalBatch(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'GroupStrategy'):
        """public com.badlogic.gdx.graphics.g3d.decals.DecalBatch(com.badlogic.gdx.graphics.g3d.decals.GroupStrategy)"""
        val = _DecalBatch(arg0)
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.DecalBatch
from builtins import str
from pyquantum_helper import override
import java.lang.Integer as _int
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.decals.DecalBatch as _DecalBatch
_DecalBatch = _DecalBatch
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DecalBatch():
    """com.badlogic.gdx.graphics.g3d.decals.DecalBatch"""
 
    @staticmethod
    def _wrap(java_value: _DecalBatch) -> 'DecalBatch':
        return DecalBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DecalBatch):
        """
        Dynamic initializer for DecalBatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DecalBatch__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DecalBatch__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getSize(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.decals.DecalBatch.getSize()"""
        return int._wrap(super(DecalBatch, self).getSize())

    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalBatch.flush()"""
        super(DecalBatch, self).flush()

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def initialize(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalBatch.initialize(int)"""
        super(_DecalBatch, self).initialize(_int.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalBatch.dispose()"""
        super(DecalBatch, self).dispose()

    @overload
    def add(self, arg0: 'Decal'):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalBatch.add(com.badlogic.gdx.graphics.g3d.decals.Decal)"""
        super(_DecalBatch, self).add(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setGroupStrategy(self, arg0: 'GroupStrategy'):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalBatch.setGroupStrategy(com.badlogic.gdx.graphics.g3d.decals.GroupStrategy)"""
        super(_DecalBatch, self).setGroupStrategy(arg0)

    @overload
    def __init__(self, arg0: int, arg1: 'GroupStrategy'):
        """public com.badlogic.gdx.graphics.g3d.decals.DecalBatch(int,com.badlogic.gdx.graphics.g3d.decals.GroupStrategy)"""
        val = _DecalBatch(_int.valueOf(arg0), arg1)
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self, arg0: 'GroupStrategy'):
        """public com.badlogic.gdx.graphics.g3d.decals.DecalBatch(com.badlogic.gdx.graphics.g3d.decals.GroupStrategy)"""
        val = _DecalBatch(arg0)
        self.__wrapper = val

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.DecalBatch 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.DecalMaterial
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.decals.DecalMaterial as _DecalMaterial
_DecalMaterial = _DecalMaterial
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DecalMaterial():
    """com.badlogic.gdx.graphics.g3d.decals.DecalMaterial"""
 
    @staticmethod
    def _wrap(java_value: _DecalMaterial) -> 'DecalMaterial':
        return DecalMaterial(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DecalMaterial):
        """
        Dynamic initializer for DecalMaterial.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DecalMaterial__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DecalMaterial__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.decals.DecalMaterial.equals(java.lang.Object)"""
        return bool._wrap(super(_DecalMaterial, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.decals.DecalMaterial.hashCode()"""
        return int._wrap(super(DecalMaterial, self).hashCode())

    @overload
    def getSrcBlendFactor(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.decals.DecalMaterial.getSrcBlendFactor()"""
        return int._wrap(super(DecalMaterial, self).getSrcBlendFactor())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def isOpaque(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.decals.DecalMaterial.isOpaque()"""
        return bool._wrap(super(DecalMaterial, self).isOpaque())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getDstBlendFactor(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.decals.DecalMaterial.getDstBlendFactor()"""
        return int._wrap(super(DecalMaterial, self).getDstBlendFactor())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.decals.DecalMaterial()"""
        val = _DecalMaterial()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.decals.DecalMaterial()"""
        val = _DecalMaterial()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalMaterial.set()"""
        super(DecalMaterial, self).set() 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.glutils.ShaderProgram as _ShaderProgram
_ShaderProgram = _ShaderProgram
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

import com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy as _SimpleOrthoGroupStrategy
_SimpleOrthoGroupStrategy = _SimpleOrthoGroupStrategy
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class SimpleOrthoGroupStrategy():
    """com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy"""
 
    @staticmethod
    def _wrap(java_value: _SimpleOrthoGroupStrategy) -> 'SimpleOrthoGroupStrategy':
        return SimpleOrthoGroupStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _SimpleOrthoGroupStrategy):
        """
        Dynamic initializer for SimpleOrthoGroupStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_SimpleOrthoGroupStrategy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_SimpleOrthoGroupStrategy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def decideGroup(self, arg0: 'Decal') -> int:
        """public int com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy.decideGroup(com.badlogic.gdx.graphics.g3d.decals.Decal)"""
        return int._wrap(super(_SimpleOrthoGroupStrategy, self).decideGroup(arg0))

    @overload
    def getGroupShader(self, arg0: int) -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy.getGroupShader(int)"""
        return 'glutils.ShaderProgram'._wrap(super(_SimpleOrthoGroupStrategy, self).getGroupShader(_int.valueOf(arg0)))

    @override
    @overload
    def afterGroup(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy.afterGroup(int)"""
        super(_SimpleOrthoGroupStrategy, self).afterGroup(_int.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy()"""
        val = _SimpleOrthoGroupStrategy()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def afterGroups(self):
        """public void com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy.afterGroups()"""
        super(SimpleOrthoGroupStrategy, self).afterGroups()

    @override
    @overload
    def beforeGroups(self):
        """public void com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy.beforeGroups()"""
        super(SimpleOrthoGroupStrategy, self).beforeGroups()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy()"""
        val = _SimpleOrthoGroupStrategy()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def beforeGroup(self, arg0: int, arg1: 'Array'):
        """public void com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy.beforeGroup(int,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.decals.Decal>)"""
        super(_SimpleOrthoGroupStrategy, self).beforeGroup(_int.valueOf(arg0), arg1)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.GroupPlug
from pyquantum_helper import import_once as _import_once
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.g3d.decals.GroupPlug as _GroupPlug
_GroupPlug = _GroupPlug
 
class GroupPlug():
    """com.badlogic.gdx.graphics.g3d.decals.GroupPlug"""
 
    @staticmethod
    def _wrap(java_value: _GroupPlug) -> 'GroupPlug':
        return GroupPlug(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GroupPlug):
        """
        Dynamic initializer for GroupPlug.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GroupPlug__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GroupPlug__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def afterGroup(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.decals.GroupPlug.afterGroup()"""
        pass

    @abstractmethod
    def beforeGroup(self, arg0: 'Array'):
        """public abstract void com.badlogic.gdx.graphics.g3d.decals.GroupPlug.beforeGroup(com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.decals.Decal>)"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
from abc import abstractmethod, ABC
import com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy as _PluggableGroupStrategy
_PluggableGroupStrategy = _PluggableGroupStrategy
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.decals.GroupStrategy as _GroupStrategy
_GroupStrategy = _GroupStrategy
from builtins import bool
import com.badlogic.gdx.graphics.g3d.decals.GroupPlug as _GroupPlug
_GroupPlug = _GroupPlug
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class PluggableGroupStrategy():
    """com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy"""
 
    @staticmethod
    def _wrap(java_value: _PluggableGroupStrategy) -> 'PluggableGroupStrategy':
        return PluggableGroupStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _PluggableGroupStrategy):
        """
        Dynamic initializer for PluggableGroupStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_PluggableGroupStrategy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_PluggableGroupStrategy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def beforeGroup(self, arg0: int, arg1: 'Array'):
        """public void com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy.beforeGroup(int,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.decals.Decal>)"""
        super(_PluggableGroupStrategy, self).beforeGroup(_int.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @abstractmethod
    def beforeGroups(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.decals.GroupStrategy.beforeGroups()"""
        pass

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @abstractmethod
    def decideGroup(self, arg0: 'Decal'):
        """public abstract int com.badlogic.gdx.graphics.g3d.decals.GroupStrategy.decideGroup(com.badlogic.gdx.graphics.g3d.decals.Decal)"""
        pass

    @abstractmethod
    def afterGroups(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.decals.GroupStrategy.afterGroups()"""
        pass

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy()"""
        val = _PluggableGroupStrategy()
        self.__wrapper = val

    @overload
    def unPlug(self, arg0: int) -> 'GroupPlug':
        """public com.badlogic.gdx.graphics.g3d.decals.GroupPlug com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy.unPlug(int)"""
        return 'GroupPlug'._wrap(super(_PluggableGroupStrategy, self).unPlug(_int.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def getGroupShader(self, arg0: int):
        """public abstract com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g3d.decals.GroupStrategy.getGroupShader(int)"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def afterGroup(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy.afterGroup(int)"""
        super(_PluggableGroupStrategy, self).afterGroup(_int.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy()"""
        val = _PluggableGroupStrategy()
        self.__wrapper = val

    @overload
    def plugIn(self, arg0: 'GroupPlug', arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy.plugIn(com.badlogic.gdx.graphics.g3d.decals.GroupPlug,int)"""
        super(_PluggableGroupStrategy, self).plugIn(arg0, _int.valueOf(arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.GroupStrategy
from pyquantum_helper import import_once as _import_once
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

import com.badlogic.gdx.graphics.g3d.decals.GroupStrategy as _GroupStrategy
_GroupStrategy = _GroupStrategy
from abc import abstractmethod, ABC
 
class GroupStrategy():
    """com.badlogic.gdx.graphics.g3d.decals.GroupStrategy"""
 
    @staticmethod
    def _wrap(java_value: _GroupStrategy) -> 'GroupStrategy':
        return GroupStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GroupStrategy):
        """
        Dynamic initializer for GroupStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GroupStrategy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GroupStrategy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getGroupShader(self, arg0: int):
        """public abstract com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g3d.decals.GroupStrategy.getGroupShader(int)"""
        pass

    @abstractmethod
    def beforeGroup(self, arg0: int, arg1: 'Array'):
        """public abstract void com.badlogic.gdx.graphics.g3d.decals.GroupStrategy.beforeGroup(int,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.decals.Decal>)"""
        pass

    @abstractmethod
    def beforeGroups(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.decals.GroupStrategy.beforeGroups()"""
        pass

    @abstractmethod
    def afterGroup(self, arg0: int):
        """public abstract void com.badlogic.gdx.graphics.g3d.decals.GroupStrategy.afterGroup(int)"""
        pass

    @abstractmethod
    def decideGroup(self, arg0: 'Decal'):
        """public abstract int com.badlogic.gdx.graphics.g3d.decals.GroupStrategy.decideGroup(com.badlogic.gdx.graphics.g3d.decals.Decal)"""
        pass

    @abstractmethod
    def afterGroups(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.decals.GroupStrategy.afterGroups()"""
        pass 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.Decal
from pyquantum_helper import import_once as _import_once
import com.badlogic.gdx.math.Vector3 as _Vector3
_Vector3 = _Vector3
import com.badlogic.gdx.graphics.g2d.TextureRegion as _TextureRegion
_TextureRegion = _TextureRegion
from builtins import str
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = _import_once("pygdx.graphics.g2d")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.graphics.g3d.decals.Decal as _Decal
_Decal = _Decal
import com.badlogic.gdx.math.Quaternion as _Quaternion
_Quaternion = _Quaternion
from typing import List
import java.lang.Float as _float
import com.badlogic.gdx.graphics.Color as _Color
_Color = _Color
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.graphics.g3d.decals.DecalMaterial as _DecalMaterial
_DecalMaterial = _DecalMaterial
try:
    from pygdx import math
except ImportError:
    math = _import_once("pygdx.math")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Decal():
    """com.badlogic.gdx.graphics.g3d.decals.Decal"""
 
    @staticmethod
    def _wrap(java_value: _Decal) -> 'Decal':
        return Decal(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Decal):
        """
        Dynamic initializer for Decal.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Decal__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Decal__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def newDecal(arg0: float, arg1: float, arg2: 'TextureRegion', arg3: int, arg4: int) -> 'Decal':
        """public static com.badlogic.gdx.graphics.g3d.decals.Decal com.badlogic.gdx.graphics.g3d.decals.Decal.newDecal(float,float,com.badlogic.gdx.graphics.g2d.TextureRegion,int,int)"""
        return Decal._wrap(_Decal.newDecal(_float.valueOf(arg0), _float.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4)))

    @overload
    def setRotation(self, arg0: 'Quaternion'):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setRotation(com.badlogic.gdx.math.Quaternion)"""
        super(_Decal, self).setRotation(arg0)

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.decals.Decal.getHeight()"""
        return float._wrap(super(Decal, self).getHeight())

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.decals.Decal.getX()"""
        return float._wrap(super(Decal, self).getX())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.decals.Decal()"""
        val = _Decal()
        self.__wrapper = val

    @overload
    def getRotation(self) -> 'math.Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.graphics.g3d.decals.Decal.getRotation()"""
        return 'math.Quaternion'._wrap(super(Decal, self).getRotation())

    @overload
    def setHeight(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setHeight(float)"""
        super(_Decal, self).setHeight(_float.valueOf(arg0))

    @overload
    def setRotationX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setRotationX(float)"""
        super(_Decal, self).setRotationX(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.decals.Decal.getScaleY()"""
        return float._wrap(super(Decal, self).getScaleY())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def translateX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.translateX(float)"""
        super(_Decal, self).translateX(_float.valueOf(arg0))

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.decals.Decal.getScaleX()"""
        return float._wrap(super(Decal, self).getScaleX())

    @overload
    def setPosition(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setPosition(com.badlogic.gdx.math.Vector3)"""
        super(_Decal, self).setPosition(arg0)

    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g3d.decals.Decal.getVertices()"""
        return List[float]._wrap(super(Decal, self).getVertices())

    @overload
    def setScaleY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setScaleY(float)"""
        super(_Decal, self).setScaleY(_float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g3d.decals.Decal.getColor()"""
        return 'graphics.Color'._wrap(super(Decal, self).getColor())

    @overload
    def setWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setWidth(float)"""
        super(_Decal, self).setWidth(_float.valueOf(arg0))

    @overload
    def getTextureRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.graphics.g3d.decals.Decal.getTextureRegion()"""
        return 'g2d.TextureRegion'._wrap(super(Decal, self).getTextureRegion())

    @overload
    def getPosition(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.decals.Decal.getPosition()"""
        return 'math.Vector3'._wrap(super(Decal, self).getPosition())

    @staticmethod
    @overload
    def newDecal(arg0: float, arg1: float, arg2: 'TextureRegion', arg3: int, arg4: int, arg5: 'DecalMaterial') -> 'Decal':
        """public static com.badlogic.gdx.graphics.g3d.decals.Decal com.badlogic.gdx.graphics.g3d.decals.Decal.newDecal(float,float,com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,com.badlogic.gdx.graphics.g3d.decals.DecalMaterial)"""
        return Decal._wrap(_Decal.newDecal(_float.valueOf(arg0), _float.valueOf(arg1), arg2, _int.valueOf(arg3), _int.valueOf(arg4), arg5))

    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setScale(float,float)"""
        super(_Decal, self).setScale(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def setMaterial(self, arg0: 'DecalMaterial'):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setMaterial(com.badlogic.gdx.graphics.g3d.decals.DecalMaterial)"""
        super(_Decal, self).setMaterial(arg0)

    @staticmethod
    @overload
    def newDecal(arg0: float, arg1: float, arg2: 'TextureRegion', arg3: bool) -> 'Decal':
        """public static com.badlogic.gdx.graphics.g3d.decals.Decal com.badlogic.gdx.graphics.g3d.decals.Decal.newDecal(float,float,com.badlogic.gdx.graphics.g2d.TextureRegion,boolean)"""
        return Decal._wrap(_Decal.newDecal(_float.valueOf(arg0), _float.valueOf(arg1), arg2, _boolean.valueOf(arg3)))

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setColor(float,float,float,float)"""
        super(_Decal, self).setColor(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2), _float.valueOf(arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setRotation(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setRotation(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(_Decal, self).setRotation(arg0, arg1)

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setY(float)"""
        super(_Decal, self).setY(_float.valueOf(arg0))

    @overload
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setPackedColor(float)"""
        super(_Decal, self).setPackedColor(_float.valueOf(arg0))

    @overload
    def lookAt(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.lookAt(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(_Decal, self).lookAt(arg0, arg1)

    @overload
    def translateZ(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.translateZ(float)"""
        super(_Decal, self).translateZ(_float.valueOf(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setPosition(float,float,float)"""
        super(_Decal, self).setPosition(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setColor(com.badlogic.gdx.graphics.Color)"""
        super(_Decal, self).setColor(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def setRotationZ(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setRotationZ(float)"""
        super(_Decal, self).setRotationZ(_float.valueOf(arg0))

    @overload
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(_Decal, self).setTextureRegion(arg0)

    @overload
    def rotateY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.rotateY(float)"""
        super(_Decal, self).rotateY(_float.valueOf(arg0))

    @staticmethod
    @overload
    def newDecal(arg0: 'TextureRegion', arg1: bool) -> 'Decal':
        """public static com.badlogic.gdx.graphics.g3d.decals.Decal com.badlogic.gdx.graphics.g3d.decals.Decal.newDecal(com.badlogic.gdx.graphics.g2d.TextureRegion,boolean)"""
        return Decal._wrap(_Decal.newDecal(arg0, _boolean.valueOf(arg1)))

    @overload
    def translate(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.translate(com.badlogic.gdx.math.Vector3)"""
        super(_Decal, self).translate(arg0)

    @overload
    def getMaterial(self) -> 'DecalMaterial':
        """public com.badlogic.gdx.graphics.g3d.decals.DecalMaterial com.badlogic.gdx.graphics.g3d.decals.Decal.getMaterial()"""
        return 'DecalMaterial'._wrap(super(Decal, self).getMaterial())

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.decals.Decal.getWidth()"""
        return float._wrap(super(Decal, self).getWidth())

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setScale(float)"""
        super(_Decal, self).setScale(_float.valueOf(arg0))

    @overload
    def setRotationY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setRotationY(float)"""
        super(_Decal, self).setRotationY(_float.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.decals.Decal()"""
        val = _Decal()
        self.__wrapper = val

    @overload
    def rotateZ(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.rotateZ(float)"""
        super(_Decal, self).rotateZ(_float.valueOf(arg0))

    @staticmethod
    @overload
    def newDecal(arg0: 'TextureRegion') -> 'Decal':
        """public static com.badlogic.gdx.graphics.g3d.decals.Decal com.badlogic.gdx.graphics.g3d.decals.Decal.newDecal(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return Decal._wrap(_Decal.newDecal(arg0))

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setX(float)"""
        super(_Decal, self).setX(_float.valueOf(arg0))

    @overload
    def translateY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.translateY(float)"""
        super(_Decal, self).translateY(_float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: 'DecalMaterial'):
        """public com.badlogic.gdx.graphics.g3d.decals.Decal(com.badlogic.gdx.graphics.g3d.decals.DecalMaterial)"""
        val = _Decal(arg0)
        self.__wrapper = val

    @overload
    def rotateX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.rotateX(float)"""
        super(_Decal, self).rotateX(_float.valueOf(arg0))

    @staticmethod
    @overload
    def newDecal(arg0: float, arg1: float, arg2: 'TextureRegion') -> 'Decal':
        """public static com.badlogic.gdx.graphics.g3d.decals.Decal com.badlogic.gdx.graphics.g3d.decals.Decal.newDecal(float,float,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return Decal._wrap(_Decal.newDecal(_float.valueOf(arg0), _float.valueOf(arg1), arg2))

    @overload
    def getZ(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.decals.Decal.getZ()"""
        return float._wrap(super(Decal, self).getZ())

    @overload
    def setDimensions(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setDimensions(float,float)"""
        super(_Decal, self).setDimensions(_float.valueOf(arg0), _float.valueOf(arg1))

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.decals.Decal.getY()"""
        return float._wrap(super(Decal, self).getY())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.translate(float,float,float)"""
        super(_Decal, self).translate(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def setRotation(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setRotation(float,float,float)"""
        super(_Decal, self).setRotation(_float.valueOf(arg0), _float.valueOf(arg1), _float.valueOf(arg2))

    @overload
    def setBlending(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setBlending(int,int)"""
        super(_Decal, self).setBlending(_int.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def setZ(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setZ(float)"""
        super(_Decal, self).setZ(_float.valueOf(arg0))

    @overload
    def setScaleX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setScaleX(float)"""
        super(_Decal, self).setScaleX(_float.valueOf(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy
from pyquantum_helper import import_once as _import_once
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = _import_once("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy as _CameraGroupStrategy
_CameraGroupStrategy = _CameraGroupStrategy
import com.badlogic.gdx.graphics.Camera as _Camera
_Camera = _Camera
import com.badlogic.gdx.graphics.glutils.ShaderProgram as _ShaderProgram
_ShaderProgram = _ShaderProgram
import java.lang.String as _String
_String = _String
import java.util.Comparator as Comparator
import java.lang.Integer as _int
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = _import_once("pygdx.graphics.glutils")

try:
    from pygdx import graphics
except ImportError:
    graphics = _import_once("pygdx.graphics")

from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CameraGroupStrategy():
    """com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy"""
 
    @staticmethod
    def _wrap(java_value: _CameraGroupStrategy) -> 'CameraGroupStrategy':
        return CameraGroupStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CameraGroupStrategy):
        """
        Dynamic initializer for CameraGroupStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CameraGroupStrategy__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CameraGroupStrategy__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def decideGroup(self, arg0: 'Decal') -> int:
        """public int com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.decideGroup(com.badlogic.gdx.graphics.g3d.decals.Decal)"""
        return int._wrap(super(_CameraGroupStrategy, self).decideGroup(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.dispose()"""
        super(CameraGroupStrategy, self).dispose()

    @overload
    def getGroupShader(self, arg0: int) -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.getGroupShader(int)"""
        return 'glutils.ShaderProgram'._wrap(super(_CameraGroupStrategy, self).getGroupShader(_int.valueOf(arg0)))

    @overload
    def __init__(self, arg0: 'Camera'):
        """public com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy(com.badlogic.gdx.graphics.Camera)"""
        val = _CameraGroupStrategy(arg0)
        self.__wrapper = val

    @override
    @overload
    def beforeGroup(self, arg0: int, arg1: 'Array'):
        """public void com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.beforeGroup(int,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.decals.Decal>)"""
        super(_CameraGroupStrategy, self).beforeGroup(_int.valueOf(arg0), arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def afterGroups(self):
        """public void com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.afterGroups()"""
        super(CameraGroupStrategy, self).afterGroups()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(_CameraGroupStrategy, self).setCamera(arg0)

    @override
    @overload
    def beforeGroups(self):
        """public void com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.beforeGroups()"""
        super(CameraGroupStrategy, self).beforeGroups()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def afterGroup(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.afterGroup(int)"""
        super(_CameraGroupStrategy, self).afterGroup(_int.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'Camera', arg1: 'Comparator'):
        """public com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy(com.badlogic.gdx.graphics.Camera,java.util.Comparator<com.badlogic.gdx.graphics.g3d.decals.Decal>)"""
        val = _CameraGroupStrategy(arg0, arg1)
        self.__wrapper = val

    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.getCamera()"""
        return 'graphics.Camera'._wrap(super(CameraGroupStrategy, self).getCamera())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())