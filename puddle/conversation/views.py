from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from item.models import Item

from .models import Conversation
from .forms import ConversationMessageForm


@login_required
def new_conversation(request, item_pk):
    """View for creating a new conversation."""

    item = get_object_or_404(Item, pk=item_pk)

    # Prevent the item owner from starting a conversation with themselves
    if item.created_by == request.user:
        return redirect('dashboard:index')

    # Check if a conversation already exists
    conversations = Conversation.objects.filter(
        item=item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversation:detail', pk=conversations[0].pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            # Create a new conversation
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            # Add the first message to the conversation
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.sender = request.user  # Set the sender field
            conversation_message.save()

            return redirect('item:detail', pk=item.pk)
    else:
        form = ConversationMessageForm()

    # Render the form for creating a new conversation
    return render(request, 'conversation/new.html', {
        'form': form,
    })


@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request, 'conversation/inbox.html', {
        'conversations': conversations,
    })


@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(
        members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)

        if form.is_valid():
            # Add the message to the conversation
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.sender = request.user
            conversation_message.save()

            conversation.save()  # Save the conversation again to update the last message timestamp

            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form,
    })
