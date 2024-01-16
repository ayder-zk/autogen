from dataclasses import dataclass
from typing import Any, Union, Dict, List, Optional
from functools import partialmethod

from autogen.agentchat.agent import Agent


class AgentCallbackHandler:

    def on_send(
            self,
            agent: Agent,
            message: Union[Dict, str],
            recipient: Agent,
            **kwargs: Any
    ) -> Any:
        """Run on the agent sends a message from the recipient."""

    async def on_a_send(
            self,
            agent: Agent,
            message: Union[Dict, str],
            recipient: Agent,
            **kwargs: Any
    ) -> Any:
        """
        (async) Run on the agent sends the message from the recipient.
        """

    def on_receive(
            self,
            agent: Agent,
            message: Union[Dict, str],
            sender: Agent,
            **kwargs: Any
    ) -> Any:
        """Run on the agent receives the message from the sender."""

    async def on_a_receive(
            self,
            agent: Agent,
            message: Union[Dict, str],
            sender: Agent,
            **kwargs: Any
    ) -> Any:
        """
        (async) Run on the agent receives the message from the
        sender.
        """

    def on_generate_reply(
            self,
            agent: Agent,
            messages: Optional[List[Dict]] = None,
            sender: Optional[Agent] = None,
            **kwargs: Any
    ) -> Any:
        """Run on the agent generate reply."""

    async def on_a_generate_reply(
            self,
            agent: Agent,
            messages: Optional[List[Dict]] = None,
            sender: Optional[Agent] = None,
            **kwargs: Any
    ) -> Any:
        """(async) Run on the agent generates a reply."""

    def on_generate_final_reply(
            self,
            agent: Agent,
            reply: Union[str, Dict, None],
            messages: Optional[List[Dict]] = None,
            sender: Optional[Agent] = None,
            **kwargs: Any
    ) -> Any:
        """Run on the agent generate a final reply."""

    async def on_a_generate_final_reply(
            self,
            agent: Agent,
            reply: Union[str, Dict, None],
            messages: Optional[List[Dict]] = None,
            sender: Optional[Agent] = None,
            **kwargs: Any
    ) -> Any:
        """(async) Run on the agent generates a final reply."""

    async def on_llm_start(
            self,
            agent: Agent,
            sender: Optional[Agent] = None,
            **kwargs: Any
    ) -> Any:
        """
        (async) Run on LLM starts for the agent.
        Only available when streaming is enabled.
        """

    async def on_llm_new_token(
            self,
            agent: Agent,
            token: str,
            sender: Optional[Agent] = None,
            **kwargs: Any
    ) -> Any:
        """
        (async) Run on new LLM token received for the agent.
        Only available when streaming is enabled.
        """

    async def on_llm_end(
            self,
            agent: Agent,
            sender: Optional[Agent] = None,
            **kwargs: Any
    ) -> Any:
        """
        (async) Run on LLM ends for the agent.
        Only available when streaming is enabled.
        """

    async def on_llm_error(
            self,
            agent: Agent,
            error: BaseException,
            **kwargs: Any,
    ) -> Any:
        """Run when LLM errors."""


@dataclass
class AgentCallbackListHandler(AgentCallbackHandler):
    """Callback handler that calls a list of agent's callback
    handlers."""

    callbacks: List[AgentCallbackHandler]

    def _call(self, method, *args, **kwargs):
        for cb in self.callbacks:
            getattr(cb, method)(*args, **kwargs)

    async def _acall(self, method, *args, **kwargs):
        for cb in self.callbacks:
            await getattr(cb, method)(*args, **kwargs)

    on_send = partialmethod(_call, method='on_send')
    on_a_send = partialmethod(_acall, method='on_a_send')
    on_receive = partialmethod(_call, method='on_receive')
    on_a_receive = partialmethod(_acall, method='on_a_receive')
    on_generate_reply = partialmethod(_call, method='on_generate_reply')
    on_a_generate_reply = partialmethod(_acall, method='on_a_generate_reply')
    on_generate_final_reply = partialmethod(
        _call, method='on_generate_final_reply')
    on_a_generate_final_reply = partialmethod(
        _acall, method='on_a_generate_final_reply')
    on_llm_start = partialmethod(_acall, method='on_llm_start')
    on_llm_new_token = partialmethod(_acall, method='on_llm_new_token')
    on_llm_end = partialmethod(_acall, method='on_llm_end')
    on_llm_error = partialmethod(_acall, method='on_llm_error')
