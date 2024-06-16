import abc


class SingletonMixin(abc.ABC):

    __singleton = None

    def __new__(cls, *args, **kwargs):

        if cls.__singleton is not None:
            raise RuntimeError(
                f"Cannot have more than one {cls.__name__} instance running within the application."
            )

        cls.__singleton = super().__new__(cls)

        return cls.__singleton
