from typing import Any, Union, Dict, List, Optional

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
