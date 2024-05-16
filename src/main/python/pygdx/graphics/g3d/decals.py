from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.graphics.glutils.ShaderProgram as __ShaderProgram
__ShaderProgram = __ShaderProgram
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy as __SimpleOrthoGroupStrategy
__SimpleOrthoGroupStrategy = __SimpleOrthoGroupStrategy
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SimpleOrthoGroupStrategy(__GroupStrategy, GroupStrategy):
    """com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy"""
 
    @staticmethod
    def __wrap(java_value: __SimpleOrthoGroupStrategy) -> 'SimpleOrthoGroupStrategy':
        return SimpleOrthoGroupStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleOrthoGroupStrategy):
        """
        Dynamic initializer for SimpleOrthoGroupStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def decideGroup(self, arg0: 'Decal') -> int:
        """public int com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy.decideGroup(com.badlogic.gdx.graphics.g3d.decals.Decal)"""
        return int.__wrap(super(__SimpleOrthoGroupStrategy, self).decideGroup(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getGroupShader(self, arg0: int) -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy.getGroupShader(int)"""
        return 'glutils.ShaderProgram'.__wrap(super(__SimpleOrthoGroupStrategy, self).getGroupShader(__int.valueOf(arg0)))

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy()"""
        val = __SimpleOrthoGroupStrategy()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def beforeGroup(self, arg0: int, arg1: 'Array'):
        """public void com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy.beforeGroup(int,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.decals.Decal>)"""
        super(__SimpleOrthoGroupStrategy, self).beforeGroup(__int.valueOf(arg0), arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def afterGroup(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy.afterGroup(int)"""
        super(__SimpleOrthoGroupStrategy, self).afterGroup(__int.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy()"""
        val = __SimpleOrthoGroupStrategy()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.graphics.glutils.ShaderProgram as __ShaderProgram
__ShaderProgram = __ShaderProgram
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy as __SimpleOrthoGroupStrategy
__SimpleOrthoGroupStrategy = __SimpleOrthoGroupStrategy
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class SimpleOrthoGroupStrategy(__GroupStrategy, GroupStrategy):
    """com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy"""
 
    @staticmethod
    def __wrap(java_value: __SimpleOrthoGroupStrategy) -> 'SimpleOrthoGroupStrategy':
        return SimpleOrthoGroupStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SimpleOrthoGroupStrategy):
        """
        Dynamic initializer for SimpleOrthoGroupStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def decideGroup(self, arg0: 'Decal') -> int:
        """public int com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy.decideGroup(com.badlogic.gdx.graphics.g3d.decals.Decal)"""
        return int.__wrap(super(__SimpleOrthoGroupStrategy, self).decideGroup(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def getGroupShader(self, arg0: int) -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy.getGroupShader(int)"""
        return 'glutils.ShaderProgram'.__wrap(super(__SimpleOrthoGroupStrategy, self).getGroupShader(__int.valueOf(arg0)))

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy()"""
        val = __SimpleOrthoGroupStrategy()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def beforeGroup(self, arg0: int, arg1: 'Array'):
        """public void com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy.beforeGroup(int,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.decals.Decal>)"""
        super(__SimpleOrthoGroupStrategy, self).beforeGroup(__int.valueOf(arg0), arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def afterGroup(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy.afterGroup(int)"""
        super(__SimpleOrthoGroupStrategy, self).afterGroup(__int.valueOf(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy()"""
        val = __SimpleOrthoGroupStrategy()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.SimpleOrthoGroupStrategy 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.graphics.glutils.ShaderProgram as __ShaderProgram
__ShaderProgram = __ShaderProgram
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.Camera as __Camera
__Camera = __Camera
import java.util.Comparator as Comparator
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy as __CameraGroupStrategy
__CameraGroupStrategy = __CameraGroupStrategy
try:
    from pygdx.graphics import glutils
except ImportError:
    glutils = __import_once__("pygdx.graphics.glutils")

import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class CameraGroupStrategy(__GroupStrategy, GroupStrategy, pygdx.__Disposable, utils.Disposable):
    """com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy"""
 
    @staticmethod
    def __wrap(java_value: __CameraGroupStrategy) -> 'CameraGroupStrategy':
        return CameraGroupStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CameraGroupStrategy):
        """
        Dynamic initializer for CameraGroupStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.dispose()"""
        super(CameraGroupStrategy, self).dispose()

    @overload
    def getCamera(self) -> 'graphics.Camera':
        """public com.badlogic.gdx.graphics.Camera com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.getCamera()"""
        return 'graphics.Camera'.__wrap(super(CameraGroupStrategy, self).getCamera())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self, arg0: 'Camera'):
        """public com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy(com.badlogic.gdx.graphics.Camera)"""
        val = __CameraGroupStrategy(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def beforeGroup(self, arg0: int, arg1: 'Array'):
        """public void com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.beforeGroup(int,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.decals.Decal>)"""
        super(__CameraGroupStrategy, self).beforeGroup(__int.valueOf(arg0), arg1)

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
    def __init__(self, arg0: 'Camera', arg1: 'Comparator'):
        """public com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy(com.badlogic.gdx.graphics.Camera,java.util.Comparator<com.badlogic.gdx.graphics.g3d.decals.Decal>)"""
        val = __CameraGroupStrategy(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def beforeGroups(self):
        """public void com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.beforeGroups()"""
        super(CameraGroupStrategy, self).beforeGroups()

    @overload
    def setCamera(self, arg0: 'Camera'):
        """public void com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.setCamera(com.badlogic.gdx.graphics.Camera)"""
        super(__CameraGroupStrategy, self).setCamera(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def decideGroup(self, arg0: 'Decal') -> int:
        """public int com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.decideGroup(com.badlogic.gdx.graphics.g3d.decals.Decal)"""
        return int.__wrap(super(__CameraGroupStrategy, self).decideGroup(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getGroupShader(self, arg0: int) -> 'glutils.ShaderProgram':
        """public com.badlogic.gdx.graphics.glutils.ShaderProgram com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.getGroupShader(int)"""
        return 'glutils.ShaderProgram'.__wrap(super(__CameraGroupStrategy, self).getGroupShader(__int.valueOf(arg0)))

    @override
    @overload
    def afterGroup(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.decals.CameraGroupStrategy.afterGroup(int)"""
        super(__CameraGroupStrategy, self).afterGroup(__int.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.GroupPlug
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.graphics.g3d.decals.GroupPlug as __GroupPlug
__GroupPlug = __GroupPlug
from abc import abstractmethod, ABC
 
class GroupPlug(ABC):
    """com.badlogic.gdx.graphics.g3d.decals.GroupPlug"""
 
    @staticmethod
    def __wrap(java_value: __GroupPlug) -> 'GroupPlug':
        return GroupPlug(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GroupPlug):
        """
        Dynamic initializer for GroupPlug.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
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
from pyquantum_helper import import_once as __import_once__
from builtins import str
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy as __PluggableGroupStrategy
__PluggableGroupStrategy = __PluggableGroupStrategy
from abc import abstractmethod, ABC
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.graphics.g3d.decals.GroupStrategy as __GroupStrategy
__GroupStrategy = __GroupStrategy
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.graphics.g3d.decals.GroupPlug as __GroupPlug
__GroupPlug = __GroupPlug
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class PluggableGroupStrategy(ABC, __GroupStrategy, GroupStrategy):
    """com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy"""
 
    @staticmethod
    def __wrap(java_value: __PluggableGroupStrategy) -> 'PluggableGroupStrategy':
        return PluggableGroupStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __PluggableGroupStrategy):
        """
        Dynamic initializer for PluggableGroupStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def plugIn(self, arg0: 'GroupPlug', arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy.plugIn(com.badlogic.gdx.graphics.g3d.decals.GroupPlug,int)"""
        super(__PluggableGroupStrategy, self).plugIn(arg0, __int.valueOf(arg1))

    @override
    @overload
    def afterGroup(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy.afterGroup(int)"""
        super(__PluggableGroupStrategy, self).afterGroup(__int.valueOf(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def beforeGroup(self, arg0: int, arg1: 'Array'):
        """public void com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy.beforeGroup(int,com.badlogic.gdx.utils.Array<com.badlogic.gdx.graphics.g3d.decals.Decal>)"""
        super(__PluggableGroupStrategy, self).beforeGroup(__int.valueOf(arg0), arg1)

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @abstractmethod
    def decideGroup(self, arg0: 'Decal'):
        """public abstract int com.badlogic.gdx.graphics.g3d.decals.GroupStrategy.decideGroup(com.badlogic.gdx.graphics.g3d.decals.Decal)"""
        pass

    @abstractmethod
    def afterGroups(self, ):
        """public abstract void com.badlogic.gdx.graphics.g3d.decals.GroupStrategy.afterGroups()"""
        pass

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy()"""
        val = __PluggableGroupStrategy()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy()"""
        val = __PluggableGroupStrategy()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def unPlug(self, arg0: int) -> 'GroupPlug':
        """public com.badlogic.gdx.graphics.g3d.decals.GroupPlug com.badlogic.gdx.graphics.g3d.decals.PluggableGroupStrategy.unPlug(int)"""
        return 'GroupPlug'.__wrap(super(__PluggableGroupStrategy, self).unPlug(__int.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.GroupStrategy
from pyquantum_helper import import_once as __import_once__
try:
    from pygdx import utils
except ImportError:
    utils = __import_once__("pygdx.utils")

import com.badlogic.gdx.graphics.g3d.decals.GroupStrategy as __GroupStrategy
__GroupStrategy = __GroupStrategy
from abc import abstractmethod, ABC
 
class GroupStrategy(ABC):
    """com.badlogic.gdx.graphics.g3d.decals.GroupStrategy"""
 
    @staticmethod
    def __wrap(java_value: __GroupStrategy) -> 'GroupStrategy':
        return GroupStrategy(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GroupStrategy):
        """
        Dynamic initializer for GroupStrategy.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
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
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.DecalBatch
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import com.badlogic.gdx.graphics.g3d.decals.DecalBatch as __DecalBatch
__DecalBatch = __DecalBatch
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DecalBatch(pygdx.__Disposable, utils.Disposable):
    """com.badlogic.gdx.graphics.g3d.decals.DecalBatch"""
 
    @staticmethod
    def __wrap(java_value: __DecalBatch) -> 'DecalBatch':
        return DecalBatch(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DecalBatch):
        """
        Dynamic initializer for DecalBatch.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def flush(self):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalBatch.flush()"""
        super(DecalBatch, self).flush()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def setGroupStrategy(self, arg0: 'GroupStrategy'):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalBatch.setGroupStrategy(com.badlogic.gdx.graphics.g3d.decals.GroupStrategy)"""
        super(__DecalBatch, self).setGroupStrategy(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSize(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.decals.DecalBatch.getSize()"""
        return int.__wrap(super(DecalBatch, self).getSize())

    @overload
    def initialize(self, arg0: int):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalBatch.initialize(int)"""
        super(__DecalBatch, self).initialize(__int.valueOf(arg0))

    @override
    @overload
    def dispose(self):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalBatch.dispose()"""
        super(DecalBatch, self).dispose()

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, arg0: int, arg1: 'GroupStrategy'):
        """public com.badlogic.gdx.graphics.g3d.decals.DecalBatch(int,com.badlogic.gdx.graphics.g3d.decals.GroupStrategy)"""
        val = __DecalBatch(__int.valueOf(arg0), arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: 'GroupStrategy'):
        """public com.badlogic.gdx.graphics.g3d.decals.DecalBatch(com.badlogic.gdx.graphics.g3d.decals.GroupStrategy)"""
        val = __DecalBatch(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def add(self, arg0: 'Decal'):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalBatch.add(com.badlogic.gdx.graphics.g3d.decals.Decal)"""
        super(__DecalBatch, self).add(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.Decal
from pyquantum_helper import import_once as __import_once__
import com.badlogic.gdx.graphics.Color as __Color
__Color = __Color
import com.badlogic.gdx.graphics.g3d.decals.DecalMaterial as __DecalMaterial
__DecalMaterial = __DecalMaterial
from builtins import str
import com.badlogic.gdx.graphics.g3d.decals.Decal as __Decal
__Decal = __Decal
import java.lang.Boolean as __boolean
from pyquantum_helper import override
try:
    from pygdx.graphics import g2d
except ImportError:
    g2d = __import_once__("pygdx.graphics.g2d")

import java.lang.Object as __object
from builtins import type
import com.badlogic.gdx.math.Vector3 as __Vector3
__Vector3 = __Vector3
from builtins import float
import com.badlogic.gdx.math.Quaternion as __Quaternion
__Quaternion = __Quaternion
from typing import List
import com.badlogic.gdx.graphics.g2d.TextureRegion as __TextureRegion
__TextureRegion = __TextureRegion
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
try:
    from pygdx import math
except ImportError:
    math = __import_once__("pygdx.math")

import java.lang.Integer as __int
try:
    from pygdx import graphics
except ImportError:
    graphics = __import_once__("pygdx.graphics")

from builtins import bool
from builtins import int
 
class Decal():
    """com.badlogic.gdx.graphics.g3d.decals.Decal"""
 
    @staticmethod
    def __wrap(java_value: __Decal) -> 'Decal':
        return Decal(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Decal):
        """
        Dynamic initializer for Decal.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def setHeight(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setHeight(float)"""
        super(__Decal, self).setHeight(__float.valueOf(arg0))

    @overload
    def setPosition(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setPosition(float,float,float)"""
        super(__Decal, self).setPosition(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def getTextureRegion(self) -> 'g2d.TextureRegion':
        """public com.badlogic.gdx.graphics.g2d.TextureRegion com.badlogic.gdx.graphics.g3d.decals.Decal.getTextureRegion()"""
        return 'g2d.TextureRegion'.__wrap(super(Decal, self).getTextureRegion())

    @overload
    def setMaterial(self, arg0: 'DecalMaterial'):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setMaterial(com.badlogic.gdx.graphics.g3d.decals.DecalMaterial)"""
        super(__Decal, self).setMaterial(arg0)

    @overload
    def rotateZ(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.rotateZ(float)"""
        super(__Decal, self).rotateZ(__float.valueOf(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setColor(self, arg0: 'Color'):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setColor(com.badlogic.gdx.graphics.Color)"""
        super(__Decal, self).setColor(arg0)

    @overload
    def setPackedColor(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setPackedColor(float)"""
        super(__Decal, self).setPackedColor(__float.valueOf(arg0))

    @overload
    def getX(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.decals.Decal.getX()"""
        return float.__wrap(super(Decal, self).getX())

    @overload
    def getColor(self) -> 'graphics.Color':
        """public com.badlogic.gdx.graphics.Color com.badlogic.gdx.graphics.g3d.decals.Decal.getColor()"""
        return 'graphics.Color'.__wrap(super(Decal, self).getColor())

    @overload
    def getHeight(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.decals.Decal.getHeight()"""
        return float.__wrap(super(Decal, self).getHeight())

    @overload
    def setX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setX(float)"""
        super(__Decal, self).setX(__float.valueOf(arg0))

    @overload
    def setRotation(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setRotation(float,float,float)"""
        super(__Decal, self).setRotation(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.decals.Decal()"""
        val = __Decal()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def setY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setY(float)"""
        super(__Decal, self).setY(__float.valueOf(arg0))

    @overload
    def setZ(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setZ(float)"""
        super(__Decal, self).setZ(__float.valueOf(arg0))

    @overload
    def setPosition(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setPosition(com.badlogic.gdx.math.Vector3)"""
        super(__Decal, self).setPosition(arg0)

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.decals.Decal()"""
        val = __Decal()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def setRotationX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setRotationX(float)"""
        super(__Decal, self).setRotationX(__float.valueOf(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def getRotation(self) -> 'math.Quaternion':
        """public com.badlogic.gdx.math.Quaternion com.badlogic.gdx.graphics.g3d.decals.Decal.getRotation()"""
        return 'math.Quaternion'.__wrap(super(Decal, self).getRotation())

    @overload
    def rotateX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.rotateX(float)"""
        super(__Decal, self).rotateX(__float.valueOf(arg0))

    @overload
    def setTextureRegion(self, arg0: 'TextureRegion'):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setTextureRegion(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        super(__Decal, self).setTextureRegion(arg0)

    @overload
    def setDimensions(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setDimensions(float,float)"""
        super(__Decal, self).setDimensions(__float.valueOf(arg0), __float.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def translateY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.translateY(float)"""
        super(__Decal, self).translateY(__float.valueOf(arg0))

    @overload
    def getY(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.decals.Decal.getY()"""
        return float.__wrap(super(Decal, self).getY())

    @overload
    def getMaterial(self) -> 'DecalMaterial':
        """public com.badlogic.gdx.graphics.g3d.decals.DecalMaterial com.badlogic.gdx.graphics.g3d.decals.Decal.getMaterial()"""
        return 'DecalMaterial'.__wrap(super(Decal, self).getMaterial())

    @overload
    def setWidth(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setWidth(float)"""
        super(__Decal, self).setWidth(__float.valueOf(arg0))

    @overload
    def translateX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.translateX(float)"""
        super(__Decal, self).translateX(__float.valueOf(arg0))

    @overload
    def getPosition(self) -> 'math.Vector3':
        """public com.badlogic.gdx.math.Vector3 com.badlogic.gdx.graphics.g3d.decals.Decal.getPosition()"""
        return 'math.Vector3'.__wrap(super(Decal, self).getPosition())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def newDecal(arg0: float, arg1: float, arg2: 'TextureRegion', arg3: bool) -> 'Decal':
        """public static com.badlogic.gdx.graphics.g3d.decals.Decal com.badlogic.gdx.graphics.g3d.decals.Decal.newDecal(float,float,com.badlogic.gdx.graphics.g2d.TextureRegion,boolean)"""
        return Decal.__wrap(__Decal.newDecal(__float.valueOf(arg0), __float.valueOf(arg1), arg2, __boolean.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getScaleY(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.decals.Decal.getScaleY()"""
        return float.__wrap(super(Decal, self).getScaleY())

    @overload
    def lookAt(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.lookAt(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__Decal, self).lookAt(arg0, arg1)

    @overload
    def translate(self, arg0: float, arg1: float, arg2: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.translate(float,float,float)"""
        super(__Decal, self).translate(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2))

    @overload
    def getZ(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.decals.Decal.getZ()"""
        return float.__wrap(super(Decal, self).getZ())

    @overload
    def setColor(self, arg0: float, arg1: float, arg2: float, arg3: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setColor(float,float,float,float)"""
        super(__Decal, self).setColor(__float.valueOf(arg0), __float.valueOf(arg1), __float.valueOf(arg2), __float.valueOf(arg3))

    @overload
    def translateZ(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.translateZ(float)"""
        super(__Decal, self).translateZ(__float.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def translate(self, arg0: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.translate(com.badlogic.gdx.math.Vector3)"""
        super(__Decal, self).translate(arg0)

    @staticmethod
    @overload
    def newDecal(arg0: 'TextureRegion') -> 'Decal':
        """public static com.badlogic.gdx.graphics.g3d.decals.Decal com.badlogic.gdx.graphics.g3d.decals.Decal.newDecal(com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return Decal.__wrap(__Decal.newDecal(arg0))

    @overload
    def getScaleX(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.decals.Decal.getScaleX()"""
        return float.__wrap(super(Decal, self).getScaleX())

    @overload
    def setScale(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setScale(float)"""
        super(__Decal, self).setScale(__float.valueOf(arg0))

    @overload
    def setRotation(self, arg0: 'Vector3', arg1: 'Vector3'):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setRotation(com.badlogic.gdx.math.Vector3,com.badlogic.gdx.math.Vector3)"""
        super(__Decal, self).setRotation(arg0, arg1)

    @overload
    def setScaleX(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setScaleX(float)"""
        super(__Decal, self).setScaleX(__float.valueOf(arg0))

    @staticmethod
    @overload
    def newDecal(arg0: 'TextureRegion', arg1: bool) -> 'Decal':
        """public static com.badlogic.gdx.graphics.g3d.decals.Decal com.badlogic.gdx.graphics.g3d.decals.Decal.newDecal(com.badlogic.gdx.graphics.g2d.TextureRegion,boolean)"""
        return Decal.__wrap(__Decal.newDecal(arg0, __boolean.valueOf(arg1)))

    @overload
    def setBlending(self, arg0: int, arg1: int):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setBlending(int,int)"""
        super(__Decal, self).setBlending(__int.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def getWidth(self) -> float:
        """public float com.badlogic.gdx.graphics.g3d.decals.Decal.getWidth()"""
        return float.__wrap(super(Decal, self).getWidth())

    @overload
    def setRotationY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setRotationY(float)"""
        super(__Decal, self).setRotationY(__float.valueOf(arg0))

    @staticmethod
    @overload
    def newDecal(arg0: float, arg1: float, arg2: 'TextureRegion', arg3: int, arg4: int) -> 'Decal':
        """public static com.badlogic.gdx.graphics.g3d.decals.Decal com.badlogic.gdx.graphics.g3d.decals.Decal.newDecal(float,float,com.badlogic.gdx.graphics.g2d.TextureRegion,int,int)"""
        return Decal.__wrap(__Decal.newDecal(__float.valueOf(arg0), __float.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4)))

    @staticmethod
    @overload
    def newDecal(arg0: float, arg1: float, arg2: 'TextureRegion') -> 'Decal':
        """public static com.badlogic.gdx.graphics.g3d.decals.Decal com.badlogic.gdx.graphics.g3d.decals.Decal.newDecal(float,float,com.badlogic.gdx.graphics.g2d.TextureRegion)"""
        return Decal.__wrap(__Decal.newDecal(__float.valueOf(arg0), __float.valueOf(arg1), arg2))

    @overload
    def setScale(self, arg0: float, arg1: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setScale(float,float)"""
        super(__Decal, self).setScale(__float.valueOf(arg0), __float.valueOf(arg1))

    @overload
    def setScaleY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setScaleY(float)"""
        super(__Decal, self).setScaleY(__float.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def newDecal(arg0: float, arg1: float, arg2: 'TextureRegion', arg3: int, arg4: int, arg5: 'DecalMaterial') -> 'Decal':
        """public static com.badlogic.gdx.graphics.g3d.decals.Decal com.badlogic.gdx.graphics.g3d.decals.Decal.newDecal(float,float,com.badlogic.gdx.graphics.g2d.TextureRegion,int,int,com.badlogic.gdx.graphics.g3d.decals.DecalMaterial)"""
        return Decal.__wrap(__Decal.newDecal(__float.valueOf(arg0), __float.valueOf(arg1), arg2, __int.valueOf(arg3), __int.valueOf(arg4), arg5))

    @overload
    def setRotationZ(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setRotationZ(float)"""
        super(__Decal, self).setRotationZ(__float.valueOf(arg0))

    @overload
    def setRotation(self, arg0: 'Quaternion'):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.setRotation(com.badlogic.gdx.math.Quaternion)"""
        super(__Decal, self).setRotation(arg0)

    @overload
    def getVertices(self) -> List[float]:
        """public float[] com.badlogic.gdx.graphics.g3d.decals.Decal.getVertices()"""
        return List[float].__wrap(super(Decal, self).getVertices())

    @overload
    def rotateY(self, arg0: float):
        """public void com.badlogic.gdx.graphics.g3d.decals.Decal.rotateY(float)"""
        super(__Decal, self).rotateY(__float.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'DecalMaterial'):
        """public com.badlogic.gdx.graphics.g3d.decals.Decal(com.badlogic.gdx.graphics.g3d.decals.DecalMaterial)"""
        val = __Decal(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val 
 
 
# CLASS: com.badlogic.gdx.graphics.g3d.decals.DecalMaterial
import com.badlogic.gdx.graphics.g3d.decals.DecalMaterial as __DecalMaterial
__DecalMaterial = __DecalMaterial
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class DecalMaterial():
    """com.badlogic.gdx.graphics.g3d.decals.DecalMaterial"""
 
    @staticmethod
    def __wrap(java_value: __DecalMaterial) -> 'DecalMaterial':
        return DecalMaterial(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DecalMaterial):
        """
        Dynamic initializer for DecalMaterial.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__dict__ = __dynamic__.__dict__
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: object):
        return setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDstBlendFactor(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.decals.DecalMaterial.getDstBlendFactor()"""
        return int.__wrap(super(DecalMaterial, self).getDstBlendFactor())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.decals.DecalMaterial.equals(java.lang.Object)"""
        return bool.__wrap(super(__DecalMaterial, self).equals(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def isOpaque(self) -> bool:
        """public boolean com.badlogic.gdx.graphics.g3d.decals.DecalMaterial.isOpaque()"""
        return bool.__wrap(super(DecalMaterial, self).isOpaque())

    @overload
    def getSrcBlendFactor(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.decals.DecalMaterial.getSrcBlendFactor()"""
        return int.__wrap(super(DecalMaterial, self).getSrcBlendFactor())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public com.badlogic.gdx.graphics.g3d.decals.DecalMaterial()"""
        val = __DecalMaterial()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.badlogic.gdx.graphics.g3d.decals.DecalMaterial.hashCode()"""
        return int.__wrap(super(DecalMaterial, self).hashCode())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def set(self):
        """public void com.badlogic.gdx.graphics.g3d.decals.DecalMaterial.set()"""
        super(DecalMaterial, self).set()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.graphics.g3d.decals.DecalMaterial()"""
        val = __DecalMaterial()
        self.__dict__ = val.__dict__
        self.__wrapper = val