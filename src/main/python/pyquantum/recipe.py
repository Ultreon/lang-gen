from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.recipe.Recipe as __Recipe
__Recipe = __Recipe
import dev.ultreon.quantum.recipe.RecipeType as __RecipeType_RecipeDeserializer
__RecipeDeserializer = __RecipeType_RecipeDeserializer.RecipeDeserializer
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import de.marhali.json5.Json5Object as Json5Object
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.recipe.RecipeType as __RecipeType
__RecipeType = __RecipeType
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RecipeType():
    """dev.ultreon.quantum.recipe.RecipeType"""
 
    @staticmethod
    def __wrap(java_value: __RecipeType) -> 'RecipeType':
        return RecipeType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RecipeType):
        """
        Dynamic initializer for RecipeType.
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
 
    # public static final dev.ultreon.quantum.recipe.RecipeType<dev.ultreon.quantum.recipe.CraftingRecipe> dev.ultreon.quantum.recipe.RecipeType.CRAFTING
    CRAFTING: 'RecipeType' = __wrap(__RecipeType.CRAFTING)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getId(self) -> int:
        """public int dev.ultreon.quantum.recipe.RecipeType.getId()"""
        return int.__wrap(super(RecipeType, self).getId())

    @overload
    def getKey(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.recipe.RecipeType.getKey()"""
        return 'util.Identifier'.__wrap(super(RecipeType, self).getKey())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'RecipeDeserializer'):
        """public dev.ultreon.quantum.recipe.RecipeType(dev.ultreon.quantum.recipe.RecipeType$RecipeDeserializer<T>)"""
        val = __RecipeType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.recipe.RecipeType.toString()"""
        return str.__wrap(super(RecipeType, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.recipe.RecipeType.hashCode()"""
        return int.__wrap(super(RecipeType, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def deserializer(self) -> 'RecipeDeserializer':
        """public dev.ultreon.quantum.recipe.RecipeType$RecipeDeserializer<T> dev.ultreon.quantum.recipe.RecipeType.deserializer()"""
        return 'RecipeDeserializer'.__wrap(super(RecipeType, self).deserializer())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.recipe.RecipeType.equals(java.lang.Object)"""
        return bool.__wrap(super(__RecipeType, self).equals(arg0))

    @overload
    def deserialize(self, arg0: 'Identifier', arg1: 'Json5Object') -> 'Recipe':
        """public T dev.ultreon.quantum.recipe.RecipeType.deserialize(dev.ultreon.quantum.util.Identifier,de.marhali.json5.Json5Object)"""
        return 'Recipe'.__wrap(super(__RecipeType, self).deserialize(arg0, arg1))

 
 
 
# CLASS: dev.ultreon.quantum.recipe.RecipeType
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.recipe.Recipe as __Recipe
__Recipe = __Recipe
import dev.ultreon.quantum.recipe.RecipeType as __RecipeType_RecipeDeserializer
__RecipeDeserializer = __RecipeType_RecipeDeserializer.RecipeDeserializer
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import de.marhali.json5.Json5Object as Json5Object
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.recipe.RecipeType as __RecipeType
__RecipeType = __RecipeType
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class RecipeType():
    """dev.ultreon.quantum.recipe.RecipeType"""
 
    @staticmethod
    def __wrap(java_value: __RecipeType) -> 'RecipeType':
        return RecipeType(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RecipeType):
        """
        Dynamic initializer for RecipeType.
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
 
    # public static final dev.ultreon.quantum.recipe.RecipeType<dev.ultreon.quantum.recipe.CraftingRecipe> dev.ultreon.quantum.recipe.RecipeType.CRAFTING
    CRAFTING: 'RecipeType' = __wrap(__RecipeType.CRAFTING)


    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getId(self) -> int:
        """public int dev.ultreon.quantum.recipe.RecipeType.getId()"""
        return int.__wrap(super(RecipeType, self).getId())

    @overload
    def getKey(self) -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.recipe.RecipeType.getKey()"""
        return 'util.Identifier'.__wrap(super(RecipeType, self).getKey())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: 'RecipeDeserializer'):
        """public dev.ultreon.quantum.recipe.RecipeType(dev.ultreon.quantum.recipe.RecipeType$RecipeDeserializer<T>)"""
        val = __RecipeType(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.recipe.RecipeType.toString()"""
        return str.__wrap(super(RecipeType, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.recipe.RecipeType.hashCode()"""
        return int.__wrap(super(RecipeType, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def deserializer(self) -> 'RecipeDeserializer':
        """public dev.ultreon.quantum.recipe.RecipeType$RecipeDeserializer<T> dev.ultreon.quantum.recipe.RecipeType.deserializer()"""
        return 'RecipeDeserializer'.__wrap(super(RecipeType, self).deserializer())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.recipe.RecipeType.equals(java.lang.Object)"""
        return bool.__wrap(super(__RecipeType, self).equals(arg0))

    @overload
    def deserialize(self, arg0: 'Identifier', arg1: 'Json5Object') -> 'Recipe':
        """public T dev.ultreon.quantum.recipe.RecipeType.deserialize(dev.ultreon.quantum.util.Identifier,de.marhali.json5.Json5Object)"""
        return 'Recipe'.__wrap(super(__RecipeType, self).deserialize(arg0, arg1))

 
 
 
# CLASS: dev.ultreon.quantum.recipe.RecipeType 
 
 
# CLASS: dev.ultreon.quantum.recipe.Recipes
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
import java.lang.String as __String
__String = __String
from builtins import type
import dev.ultreon.quantum.recipe.Recipes as __Recipes
__Recipes = __Recipes
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class Recipes():
    """dev.ultreon.quantum.recipe.Recipes"""
 
    @staticmethod
    def __wrap(java_value: __Recipes) -> 'Recipes':
        return Recipes(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Recipes):
        """
        Dynamic initializer for Recipes.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

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

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.recipe.Recipes()"""
        val = __Recipes()
        self.__dict__ = val.__dict__
        self.__wrapper = val

        @staticmethod
        @overload
        def init():
            """public static void dev.ultreon.quantum.recipe.Recipes.init()"""
            __Recipes.init()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.recipe.Recipes()"""
        val = __Recipes()
        self.__dict__ = val.__dict__
        self.__wrapper = val

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
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.recipe.RecipeRegistry
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.util.PagedList as __PagedList
__PagedList = __PagedList
import java.util.Set as __Set
__Set = __Set
import dev.ultreon.quantum.recipe.RecipeRegistry as __RecipeRegistry
__RecipeRegistry = __RecipeRegistry
import dev.ultreon.quantum.recipe.Recipe as __Recipe
__Recipe = __Recipe
import dev.ultreon.quantum.registry.AbstractRegistry as __AbstractRegistry
__AbstractRegistry = __AbstractRegistry
from builtins import object
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.util.Set as Set
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

from builtins import int
 
class RecipeRegistry():
    """dev.ultreon.quantum.recipe.RecipeRegistry"""
 
    @staticmethod
    def __wrap(java_value: __RecipeRegistry) -> 'RecipeRegistry':
        return RecipeRegistry(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RecipeRegistry):
        """
        Dynamic initializer for RecipeRegistry.
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
    def getKey(self, arg0: 'Recipe') -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.recipe.RecipeRegistry.getKey(T)"""
        return 'util.Identifier'.__wrap(super(__RecipeRegistry, self).getKey(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def entries(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<dev.ultreon.quantum.util.Identifier, T>> dev.ultreon.quantum.recipe.RecipeRegistry.entries() throws java.lang.IllegalAccessException"""
        return 'Set'.__wrap(super(RecipeRegistry, self).entries())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def keys(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.util.Identifier> dev.ultreon.quantum.recipe.RecipeRegistry.keys()"""
        return 'List'.__wrap(super(RecipeRegistry, self).keys())

    @overload
    def __init__(self, *arg0: 'Recipe'):
        """public dev.ultreon.quantum.recipe.RecipeRegistry(T...)"""
        val = __RecipeRegistry(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def removeRecipe(self, arg0: 'Identifier') -> 'Recipe':
        """public T dev.ultreon.quantum.recipe.RecipeRegistry.removeRecipe(dev.ultreon.quantum.util.Identifier)"""
        return 'Recipe'.__wrap(super(__RecipeRegistry, self).removeRecipe(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def values(self) -> 'List':
        """public java.util.List<T> dev.ultreon.quantum.recipe.RecipeRegistry.values()"""
        return 'List'.__wrap(super(RecipeRegistry, self).values())

    @overload
    def getType(self) -> 'type.Class':
        """public java.lang.Class<T> dev.ultreon.quantum.recipe.RecipeRegistry.getType()"""
        return 'type.Class'.__wrap(super(RecipeRegistry, self).getType())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def freeze(self):
        """public void dev.ultreon.quantum.recipe.RecipeRegistry.freeze()"""
        super(RecipeRegistry, self).freeze()

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def register(self, arg0: 'Identifier', arg1: 'Recipe'):
        """public void dev.ultreon.quantum.recipe.RecipeRegistry.register(dev.ultreon.quantum.util.Identifier,T)"""
        super(__RecipeRegistry, self).register(arg0, arg1)

    @overload
    def getRecipes(self, arg0: int, arg1: 'Inventory') -> 'util.PagedList':
        """public dev.ultreon.quantum.util.PagedList<T> dev.ultreon.quantum.recipe.RecipeRegistry.getRecipes(int,dev.ultreon.quantum.menu.Inventory)"""
        return 'util.PagedList'.__wrap(super(__RecipeRegistry, self).getRecipes(__int.valueOf(arg0), arg1))

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
    def random(self) -> object:
        """public V dev.ultreon.quantum.registry.AbstractRegistry.random()"""
        return object.__wrap(super(registry.AbstractRegistry, self).random())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def get(self, arg0: 'Identifier') -> 'Recipe':
        """public T dev.ultreon.quantum.recipe.RecipeRegistry.get(dev.ultreon.quantum.util.Identifier)"""
        return 'Recipe'.__wrap(super(__RecipeRegistry, self).get(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.recipe.CraftingRecipe
from pyquantum_helper import import_once as __import_once__
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.recipe.Recipe as __Recipe
__Recipe = __Recipe
try:
    from pyquantum import item
except ImportError:
    item = __import_once__("pyquantum.item")

try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import dev.ultreon.quantum.item.ItemStack as __ItemStack
__ItemStack = __ItemStack
import de.marhali.json5.Json5Object as Json5Object
import java.lang.Object as __Object
__Object = __Object
import dev.ultreon.quantum.recipe.RecipeType as __RecipeType
__RecipeType = __RecipeType
import java.lang.Integer as __int
import dev.ultreon.quantum.recipe.CraftingRecipe as __CraftingRecipe
__CraftingRecipe = __CraftingRecipe
from builtins import bool
from builtins import int
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

import java.util.List as List
 
class CraftingRecipe():
    """dev.ultreon.quantum.recipe.CraftingRecipe"""
 
    @staticmethod
    def __wrap(java_value: __CraftingRecipe) -> 'CraftingRecipe':
        return CraftingRecipe(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CraftingRecipe):
        """
        Dynamic initializer for CraftingRecipe.
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
    def getId(self) -> 'util.Identifier':
        """public default dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.recipe.Recipe.getId()"""
        return 'util.Identifier'.__wrap(super(Recipe, self).getId())

    @override
    @overload
    def hashCode(self) -> int:
        """public int dev.ultreon.quantum.recipe.CraftingRecipe.hashCode()"""
        return int.__wrap(super(CraftingRecipe, self).hashCode())

    @overload
    def canCraft(self, arg0: 'Inventory') -> bool:
        """public boolean dev.ultreon.quantum.recipe.CraftingRecipe.canCraft(dev.ultreon.quantum.menu.Inventory)"""
        return bool.__wrap(super(__CraftingRecipe, self).canCraft(arg0))

    @override
    @overload
    def ingredients(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.recipe.CraftingRecipe.ingredients()"""
        return 'List'.__wrap(super(CraftingRecipe, self).ingredients())

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

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: 'List', arg1: 'ItemStack'):
        """public dev.ultreon.quantum.recipe.CraftingRecipe(java.util.List<dev.ultreon.quantum.item.ItemStack>,dev.ultreon.quantum.item.ItemStack)"""
        val = __CraftingRecipe(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean dev.ultreon.quantum.recipe.CraftingRecipe.equals(java.lang.Object)"""
        return bool.__wrap(super(__CraftingRecipe, self).equals(arg0))

    @override
    @overload
    def result(self) -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.recipe.CraftingRecipe.result()"""
        return 'item.ItemStack'.__wrap(super(CraftingRecipe, self).result())

    @override
    @overload
    def getType(self) -> 'RecipeType':
        """public dev.ultreon.quantum.recipe.RecipeType<dev.ultreon.quantum.recipe.CraftingRecipe> dev.ultreon.quantum.recipe.CraftingRecipe.getType()"""
        return 'RecipeType'.__wrap(super(CraftingRecipe, self).getType())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def craft(self, arg0: 'Inventory') -> 'item.ItemStack':
        """public dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.recipe.CraftingRecipe.craft(dev.ultreon.quantum.menu.Inventory)"""
        return 'item.ItemStack'.__wrap(super(__CraftingRecipe, self).craft(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String dev.ultreon.quantum.recipe.CraftingRecipe.toString()"""
        return str.__wrap(super(CraftingRecipe, self).toString())

    @staticmethod
    @overload
    def deserialize(arg0: 'Identifier', arg1: 'Json5Object') -> 'CraftingRecipe':
        """public static dev.ultreon.quantum.recipe.CraftingRecipe dev.ultreon.quantum.recipe.CraftingRecipe.deserialize(dev.ultreon.quantum.util.Identifier,de.marhali.json5.Json5Object)"""
        return CraftingRecipe.__wrap(__CraftingRecipe.deserialize(arg0, arg1)) 
 
 
# CLASS: dev.ultreon.quantum.recipe.RecipeManager
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import server
except ImportError:
    server = __import_once__("pyquantum.server")

from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.util.PagedList as __PagedList
__PagedList = __PagedList
import dev.ultreon.quantum.recipe.Recipe as __Recipe
__Recipe = __Recipe
import dev.ultreon.quantum.server.QuantumServer as __QuantumServer
__QuantumServer = __QuantumServer
import java.util.Collection as Collection
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import java.util.Collection as __Collection
__Collection = __Collection
import java.lang.Long as __long
import dev.ultreon.quantum.recipe.RecipeManager as __RecipeManager
__RecipeManager = __RecipeManager
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import java.lang.Object as __Object
__Object = __Object
try:
    from pyquantum import resources
except ImportError:
    resources = __import_once__("pyquantum.resources")

import java.lang.Integer as __int
from builtins import bool
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

from builtins import int
 
class RecipeManager():
    """dev.ultreon.quantum.recipe.RecipeManager"""
 
    @staticmethod
    def __wrap(java_value: __RecipeManager) -> 'RecipeManager':
        return RecipeManager(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RecipeManager):
        """
        Dynamic initializer for RecipeManager.
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
    def getRecipes(self, arg0: 'RecipeType') -> 'Collection':
        """public <T extends dev.ultreon.quantum.recipe.Recipe> java.util.Collection<T> dev.ultreon.quantum.recipe.RecipeManager.getRecipes(dev.ultreon.quantum.recipe.RecipeType<T>)"""
        return 'Collection'.__wrap(super(__RecipeManager, self).getRecipes(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def get(self, arg0: 'Identifier', arg1: 'RecipeType') -> 'Recipe':
        """public <T extends dev.ultreon.quantum.recipe.Recipe> T dev.ultreon.quantum.recipe.RecipeManager.get(dev.ultreon.quantum.util.Identifier,dev.ultreon.quantum.recipe.RecipeType<T>)"""
        return 'Recipe'.__wrap(super(__RecipeManager, self).get(arg0, arg1))

    @overload
    def freeze(self):
        """public void dev.ultreon.quantum.recipe.RecipeManager.freeze()"""
        super(RecipeManager, self).freeze()

    @overload
    def getKey(self, arg0: 'RecipeType', arg1: 'Recipe') -> 'util.Identifier':
        """public dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.recipe.RecipeManager.getKey(dev.ultreon.quantum.recipe.RecipeType<?>,dev.ultreon.quantum.recipe.Recipe)"""
        return 'util.Identifier'.__wrap(super(__RecipeManager, self).getKey(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def register(self, arg0: 'Identifier', arg1: 'Recipe'):
        """public <T extends dev.ultreon.quantum.recipe.Recipe> void dev.ultreon.quantum.recipe.RecipeManager.register(dev.ultreon.quantum.util.Identifier,T)"""
        super(__RecipeManager, self).register(arg0, arg1)

    @overload
    def getRecipes(self, arg0: 'RecipeType', arg1: int, arg2: 'Inventory') -> 'util.PagedList':
        """public <T extends dev.ultreon.quantum.recipe.Recipe> dev.ultreon.quantum.util.PagedList<? extends T> dev.ultreon.quantum.recipe.RecipeManager.getRecipes(dev.ultreon.quantum.recipe.RecipeType<T>,int,dev.ultreon.quantum.menu.Inventory)"""
        return 'util.PagedList'.__wrap(super(__RecipeManager, self).getRecipes(arg0, __int.valueOf(arg1), arg2))

    @overload
    def unload(self):
        """public void dev.ultreon.quantum.recipe.RecipeManager.unload()"""
        super(RecipeManager, self).unload()

    @overload
    def fireRecipeModifications(self):
        """public void dev.ultreon.quantum.recipe.RecipeManager.fireRecipeModifications()"""
        super(RecipeManager, self).fireRecipeModifications()

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
    def __init__(self, arg0: 'QuantumServer'):
        """public dev.ultreon.quantum.recipe.RecipeManager(dev.ultreon.quantum.server.QuantumServer)"""
        val = __RecipeManager(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def get() -> 'RecipeManager':
        """public static dev.ultreon.quantum.recipe.RecipeManager dev.ultreon.quantum.recipe.RecipeManager.get()"""
        return RecipeManager.__wrap(__RecipeManager.get())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def load(self, arg0: 'ResourceManager'):
        """public void dev.ultreon.quantum.recipe.RecipeManager.load(dev.ultreon.quantum.resources.ResourceManager)"""
        super(__RecipeManager, self).load(arg0)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def getServer(self) -> 'server.QuantumServer':
        """public dev.ultreon.quantum.server.QuantumServer dev.ultreon.quantum.recipe.RecipeManager.getServer()"""
        return 'server.QuantumServer'.__wrap(super(RecipeManager, self).getServer())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: dev.ultreon.quantum.recipe.RecipeType$RecipeDeserializer
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import de.marhali.json5.Json5Object as Json5Object
from abc import abstractmethod, ABC
import dev.ultreon.quantum.recipe.RecipeType as __RecipeType_RecipeDeserializer
__RecipeDeserializer = __RecipeType_RecipeDeserializer.RecipeDeserializer
 
class RecipeDeserializer(ABC):
    """dev.ultreon.quantum.recipe.RecipeType.RecipeDeserializer"""
 
    @staticmethod
    def __wrap(java_value: __RecipeDeserializer) -> 'RecipeDeserializer':
        return RecipeDeserializer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __RecipeDeserializer):
        """
        Dynamic initializer for RecipeDeserializer.
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
    def deserialize(self, arg0: 'Identifier', arg1: 'Json5Object'):
        """public abstract T dev.ultreon.quantum.recipe.RecipeType$RecipeDeserializer.deserialize(dev.ultreon.quantum.util.Identifier,de.marhali.json5.Json5Object)"""
        pass 
 
 
# CLASS: dev.ultreon.quantum.recipe.Recipe
from pyquantum_helper import import_once as __import_once__
try:
    from pyquantum import util
except ImportError:
    util = __import_once__("pyquantum.util")

import dev.ultreon.quantum.util.Identifier as __Identifier
__Identifier = __Identifier
import dev.ultreon.quantum.recipe.Recipe as __Recipe
__Recipe = __Recipe
from abc import abstractmethod, ABC
try:
    from pyquantum import menu
except ImportError:
    menu = __import_once__("pyquantum.menu")

 
class Recipe(ABC):
    """dev.ultreon.quantum.recipe.Recipe"""
 
    @staticmethod
    def __wrap(java_value: __Recipe) -> 'Recipe':
        return Recipe(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Recipe):
        """
        Dynamic initializer for Recipe.
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
    def getId(self) -> 'util.Identifier':
        """public default dev.ultreon.quantum.util.Identifier dev.ultreon.quantum.recipe.Recipe.getId()"""
        return 'util.Identifier'.__wrap(super(Recipe, self).getId())

    @abstractmethod
    def craft(self, arg0: 'Inventory'):
        """public abstract dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.recipe.Recipe.craft(dev.ultreon.quantum.menu.Inventory)"""
        pass

    @abstractmethod
    def result(self, ):
        """public abstract dev.ultreon.quantum.item.ItemStack dev.ultreon.quantum.recipe.Recipe.result()"""
        pass

    @abstractmethod
    def canCraft(self, arg0: 'Inventory'):
        """public abstract boolean dev.ultreon.quantum.recipe.Recipe.canCraft(dev.ultreon.quantum.menu.Inventory)"""
        pass

    @abstractmethod
    def getType(self, ):
        """public abstract dev.ultreon.quantum.recipe.RecipeType<?> dev.ultreon.quantum.recipe.Recipe.getType()"""
        pass

    @abstractmethod
    def ingredients(self, ):
        """public abstract java.util.List<dev.ultreon.quantum.item.ItemStack> dev.ultreon.quantum.recipe.Recipe.ingredients()"""
        pass