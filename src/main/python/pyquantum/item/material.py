from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.item.material.ItemMaterial as __ItemMaterial_Builder
__Builder = __ItemMaterial_Builder.Builder
import dev.ultreon.quantum.item.material.ItemMaterial as __ItemMaterial
__ItemMaterial = __ItemMaterial
from abc import abstractmethod, ABC
 
class ItemMaterial(ABC):
    """dev.ultreon.quantum.item.material.ItemMaterial"""
 
    @staticmethod
    def __wrap(java_value: __ItemMaterial) -> 'ItemMaterial':
        return ItemMaterial(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ItemMaterial):
        """
        Dynamic initializer for ItemMaterial.
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
 
    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static dev.ultreon.quantum.item.material.ItemMaterial$Builder dev.ultreon.quantum.item.material.ItemMaterial.builder()"""
        return Builder.__wrap(__ItemMaterial.builder())

    @abstractmethod
    def getEfficiency(self, ):
        """public abstract float dev.ultreon.quantum.item.material.ItemMaterial.getEfficiency()"""
        pass

    @abstractmethod
    def getAttackDamage(self, ):
        """public abstract float dev.ultreon.quantum.item.material.ItemMaterial.getAttackDamage()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.item.material.ItemMaterial
import dev.ultreon.quantum.item.material.ItemMaterial as __ItemMaterial_Builder
__Builder = __ItemMaterial_Builder.Builder
import dev.ultreon.quantum.item.material.ItemMaterial as __ItemMaterial
__ItemMaterial = __ItemMaterial
from abc import abstractmethod, ABC
 
class ItemMaterial(ABC):
    """dev.ultreon.quantum.item.material.ItemMaterial"""
 
    @staticmethod
    def __wrap(java_value: __ItemMaterial) -> 'ItemMaterial':
        return ItemMaterial(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ItemMaterial):
        """
        Dynamic initializer for ItemMaterial.
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
 
    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static dev.ultreon.quantum.item.material.ItemMaterial$Builder dev.ultreon.quantum.item.material.ItemMaterial.builder()"""
        return Builder.__wrap(__ItemMaterial.builder())

    @abstractmethod
    def getEfficiency(self, ):
        """public abstract float dev.ultreon.quantum.item.material.ItemMaterial.getEfficiency()"""
        pass

    @abstractmethod
    def getAttackDamage(self, ):
        """public abstract float dev.ultreon.quantum.item.material.ItemMaterial.getAttackDamage()"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.item.material.ItemMaterial 
 
 
# CLASS: dev.ultreon.quantum.item.material.ItemMaterials
import dev.ultreon.quantum.item.material.ItemMaterials as __ItemMaterials
__ItemMaterials = __ItemMaterials
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
 
class ItemMaterials():
    """dev.ultreon.quantum.item.material.ItemMaterials"""
 
    @staticmethod
    def __wrap(java_value: __ItemMaterials) -> 'ItemMaterials':
        return ItemMaterials(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ItemMaterials):
        """
        Dynamic initializer for ItemMaterials.
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
 
    # public static final dev.ultreon.quantum.item.material.ItemMaterial dev.ultreon.quantum.item.material.ItemMaterials.STONE
    STONE: 'ItemMaterial' = __wrap(__ItemMaterial.STONE)

    # public static final dev.ultreon.quantum.item.material.ItemMaterial dev.ultreon.quantum.item.material.ItemMaterials.WOOD
    WOOD: 'ItemMaterial' = __wrap(__ItemMaterial.WOOD)


    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.item.material.ItemMaterials()"""
        val = __ItemMaterials()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.item.material.ItemMaterials()"""
        val = __ItemMaterials()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.item.material.ItemMaterial$Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.item.material.ItemMaterial as __ItemMaterial_Builder
__Builder = __ItemMaterial_Builder.Builder
import java.lang.Long as __long
import java.lang.Float as __float
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.item.material.ItemMaterial as __ItemMaterial
__ItemMaterial = __ItemMaterial
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Builder():
    """dev.ultreon.quantum.item.material.ItemMaterial.Builder"""
 
    @staticmethod
    def __wrap(java_value: __Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Builder):
        """
        Dynamic initializer for Builder.
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
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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

    @overload
    def efficiency(self, arg0: float) -> 'Builder':
        """public dev.ultreon.quantum.item.material.ItemMaterial$Builder dev.ultreon.quantum.item.material.ItemMaterial$Builder.efficiency(float)"""
        return 'Builder'.__wrap(super(__Builder, self).efficiency(__float.valueOf(arg0)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def attackDamage(self, arg0: float) -> 'Builder':
        """public dev.ultreon.quantum.item.material.ItemMaterial$Builder dev.ultreon.quantum.item.material.ItemMaterial$Builder.attackDamage(float)"""
        return 'Builder'.__wrap(super(__Builder, self).attackDamage(__float.valueOf(arg0)))

    @overload
    def build(self) -> 'ItemMaterial':
        """public dev.ultreon.quantum.item.material.ItemMaterial dev.ultreon.quantum.item.material.ItemMaterial$Builder.build()"""
        return 'ItemMaterial'.__wrap(super(Builder, self).build())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.item.material.ItemMaterial$Builder()"""
        val = __Builder()
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
    def __init__(self):
        """public dev.ultreon.quantum.item.material.ItemMaterial$Builder()"""
        val = __Builder()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))